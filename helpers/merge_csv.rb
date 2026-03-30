require 'csv'

src  = "/Users/claire/code/NailPolishInventory/POLISHES-03-2026 - polishes.csv"
root = "/Users/claire/code/NailPolishInventory/polishes.csv"
data = "/Users/claire/code/NailPolishInventory/data/polishes.csv"

# Clean CRLF from source, write straight to polishes.csv
clean = File.read(src).gsub(/\r\n/, "\n").gsub(/\r/, "\n")
File.write(root, clean)
puts "polishes.csv replaced with 03-2026 data (CRLF stripped)"

# Build lookup from 03-2026: key = [number, name.downcase]
lookup = {}
CSV.parse(clean, headers: true) do |row|
  key = [row['Number'].to_s.strip, row['Name'].to_s.strip.downcase]
  lookup[key] = {
    'Name'          => row['Name'].to_s.strip,
    'Link'          => row['Link'].to_s.strip,
    'Image Address' => row['Image Address'].to_s.strip,
    'Color'         => row['Color'].to_s.strip,
    'Finish'        => row['Finish'].to_s.strip
  }
end
puts "Lookup built: #{lookup.size} entries from 03-2026"

# Also build number-only lookup for numbers that appear exactly once in 03-2026
number_count = Hash.new(0)
lookup.each { |(num, _), _| number_count[num] += 1 }
number_lookup = {}
lookup.each { |(num, _), v| number_lookup[num] = v if number_count[num] == 1 }

# Load data/polishes.csv and merge (keep Brand + LocalImage, update rest from 03-2026)
rows = CSV.read(data, headers: true)
updated = 0
name_fixes = 0

rows.each do |row|
  # Pass 1: exact number+name match
  key = [row['Number'].to_s.strip, row['Name'].to_s.strip.downcase]
  m = lookup[key]

  # Pass 2: if no exact match, try number-only (for unique numbers) and fix name too
  if m.nil?
    num = row['Number'].to_s.strip
    m = number_lookup[num]
    if m
      row['Name'] = m['Name']
      name_fixes += 1
    end
  end

  next unless m
  row['Link']          = m['Link']          unless m['Link'].empty?
  row['Image Address'] = m['Image Address'] unless m['Image Address'].empty?
  row['Color']         = m['Color']         unless m['Color'].empty?
  row['Finish']        = m['Finish']        unless m['Finish'].empty?
  updated += 1
end

CSV.open(data, 'w') { |csv| csv << rows.headers; rows.each { |r| csv << r } }

still_blank = rows.count { |r| r['Link'].to_s.strip.empty? }
puts "data/polishes.csv: #{updated} rows updated (#{name_fixes} names corrected), #{still_blank} still blank"
rows.each { |r| puts "  NO MATCH: #{r['Number']} #{r['Name']}" if r['Link'].to_s.strip.empty? }
