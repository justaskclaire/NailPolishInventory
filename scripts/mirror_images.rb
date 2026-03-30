require 'csv'
require 'net/http'
require 'uri'
require 'fileutils'

CSV_PATH = File.join(__dir__, '..', 'data', 'polishes.csv')
IMAGES_DIR = File.join(__dir__, '..', 'public', 'images')

FileUtils.mkdir_p(IMAGES_DIR)

rows = CSV.read(CSV_PATH, headers: true)
success = 0; skipped = 0; failed = 0

rows.each_with_index do |row, i|
  num = row['Number'].to_s.strip
  name = row['Name'].to_s.strip
  url = row['Image Address'].to_s.strip
  local = row['LocalImage'].to_s.strip

  # Skip if already has local image
  if !local.empty?
    skipped += 1
    next
  end

  # Skip if no URL to download
  if url.empty?
    skipped += 1
    next
  end

  # Build filename: sanitize name, infer extension from URL
  safe_name = name.gsub(/[<>:"\/\\|?*]/, '_').gsub(/\s+/, '_')[0, 120]
  ext = url.match(/\.(jpg|jpeg|png|webp|gif)/i)&.[](0) || '.jpg'
  filename = "#{num}-#{safe_name}#{ext}"
  dest = File.join(IMAGES_DIR, filename)

  # Skip if file already downloaded
  if File.exist?(dest) && File.size(dest) > 0
    row['LocalImage'] = "public/images/#{filename}"
    skipped += 1
    puts "[#{i+1}/#{rows.size}] Exists: #{filename}"
    next
  end

  # Download
  begin
    uri = URI(url)
    response = Net::HTTP.start(uri.host, uri.port, use_ssl: uri.scheme == 'https',
                                open_timeout: 15, read_timeout: 25) do |http|
      http.get(uri.request_uri, 'User-Agent' => 'NailPolishInventoryMirror/1.0')
    end

    if response.code == '200'
      File.binwrite(dest, response.body)
      row['LocalImage'] = "public/images/#{filename}"
      success += 1
      puts "[#{i+1}/#{rows.size}] Downloaded: #{filename}"
    else
      failed += 1
      puts "[#{i+1}/#{rows.size}] FAILED (HTTP #{response.code}): #{num} #{name}"
    end
  rescue => e
    failed += 1
    puts "[#{i+1}/#{rows.size}] FAILED: #{num} #{name} -> #{e.message}"
  end
end

# Write updated CSV back
CSV.open(CSV_PATH, 'w') do |csv|
  csv << rows.headers
  rows.each { |r| csv << r }
end

puts "\nDone. Downloaded: #{success}, Skipped: #{skipped}, Failed: #{failed}"
