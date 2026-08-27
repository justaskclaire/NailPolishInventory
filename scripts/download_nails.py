"""
Nail Inspo Gallery Downloader
Downloads your Pinterest "Nail Inspo" pins to a local folder.
Usage: python3 download_nails.py
"""

import urllib.request
import os
import time
import sys

URLS = [
    "https://i.pinimg.com/736x/27/c5/fa/27c5fa3b4c8d6d648f4c349a2e742356.jpg",
    "https://i.pinimg.com/736x/b1/f4/d0/b1f4d0557111cf352677039b79fc99a7.jpg",
    "https://i.pinimg.com/736x/ab/9e/85/ab9e856e4aa886921d63c372a099c082.jpg",
    "https://i.pinimg.com/736x/2d/0a/45/2d0a45eb970d8308cdc6e1badaaaef98.jpg",
    "https://i.pinimg.com/736x/96/8b/ad/968bad1ed7bbf044e0afbf9807956b16.jpg",
    "https://i.pinimg.com/736x/8f/af/4b/8faf4b95a6f4b725aa62a0ae5eef8575.jpg",
    "https://i.pinimg.com/736x/d9/96/3c/d9963c0956ede0709fc0997741cb1da8.jpg",
    "https://i.pinimg.com/736x/2c/36/4b/2c364b7f7a4a0c4dcb6978d27c8e7e1a.jpg",
    "https://i.pinimg.com/736x/53/20/03/5320038e006e4f6b90af915408002e2b.jpg",
    "https://i.pinimg.com/736x/b7/f0/5a/b7f05a0dbaae616a2db4cf13674cf18d.jpg",
    "https://i.pinimg.com/736x/53/38/d7/5338d7880d5f0145524abdd6519c7444.jpg",
    "https://i.pinimg.com/736x/27/9b/f2/279bf264c9c97011ed32d9cfcd67b90e.jpg",
    "https://i.pinimg.com/736x/28/33/5d/28335dc28ed50b66cac64937a5809848.jpg",
    "https://i.pinimg.com/736x/4f/f1/b1/4ff1b1181113ddee1044ee7f712ef409.jpg",
    "https://i.pinimg.com/736x/80/d6/12/80d612085dd28eb29566b221f18780d4.jpg",
    "https://i.pinimg.com/736x/90/e9/d0/90e9d0051857756e68e16f7d76e7b2f2.jpg",
    "https://i.pinimg.com/736x/46/0e/56/460e56dc5af8259c7c9ed00af0cc319b.jpg",
    "https://i.pinimg.com/736x/2c/a7/59/2ca759806494763b677b1a5c8e444c32.jpg",
    "https://i.pinimg.com/736x/d6/5f/4c/d65f4c350dc816a207312a0f7fc51f23.jpg",
    "https://i.pinimg.com/736x/f9/a2/a7/f9a2a7de79cc811a4d1fa1953d4da109.jpg",
    "https://i.pinimg.com/736x/db/e6/2e/dbe62eab89c9c83bcc7f9fd759b14a1e.jpg",
    "https://i.pinimg.com/736x/49/9e/e1/499ee1482ab99c105ab56a5f99441ec0.jpg",
    "https://i.pinimg.com/736x/54/8f/dc/548fdc82ed6650529c5fcff2ffa82c29.jpg",
    "https://i.pinimg.com/736x/2d/c7/fe/2dc7fe56395921d53750ede349642c30.jpg",
    "https://i.pinimg.com/736x/46/84/7a/46847a0bca3c482e93693f101e2c6276.jpg",
    "https://i.pinimg.com/736x/53/d7/96/53d796e0a6656d0f9140eeaa32529664.jpg",
    "https://i.pinimg.com/736x/8e/4b/fe/8e4bfe5c5bad931859afc3e3311dce30.jpg",
    "https://i.pinimg.com/736x/a5/30/47/a53047a316f63736ac0a3d9250932864.jpg",
    "https://i.pinimg.com/736x/04/61/9a/04619a437d8b2efb60fbb5ad976d05a2.jpg",
    "https://i.pinimg.com/736x/9f/de/24/9fde24830af8a77012e238c56a0435c7.jpg",
    "https://i.pinimg.com/736x/cb/c8/5e/cbc85e1513caea14c11fc787077ff8f9.jpg",
    "https://i.pinimg.com/736x/29/86/bd/2986bdea3a7f0f81da6d7751053de491.jpg",
    "https://i.pinimg.com/736x/87/8a/4d/878a4de54c5368c5f6356dd4c22a4b49.jpg",
    "https://i.pinimg.com/736x/19/51/3b/19513bd786a8765ad11d370662942c95.jpg",
    "https://i.pinimg.com/736x/fd/50/ae/fd50ae5ba3947e1a047b1ba22eba9cac.jpg",
    "https://i.pinimg.com/736x/da/30/0f/da300f5fab74e1e9b86e6c4a0c436d64.jpg",
    "https://i.pinimg.com/736x/9c/66/50/9c6650989178440e17e8c197c8869c43.jpg",
    "https://i.pinimg.com/736x/6a/34/47/6a344740507fcc22ff0a77289dc255c0.jpg",
    "https://i.pinimg.com/736x/9e/0a/1a/9e0a1a383903cb3d360b09ff373533a2.jpg",
    "https://i.pinimg.com/736x/5c/1a/6a/5c1a6a4a25feab822888db0e0967263e.jpg",
    "https://i.pinimg.com/736x/a5/ed/88/a5ed8899ec806ba8ceb6788eb2d51098.jpg",
    "https://i.pinimg.com/736x/50/df/1c/50df1ccc10864f002156d313d3f34787.jpg",
    "https://i.pinimg.com/736x/f2/5b/d3/f25bd30d529928991225db862a066342.jpg",
    "https://i.pinimg.com/736x/af/2b/5c/af2b5c401aceff6acac4ce4692e68077.jpg",
    "https://i.pinimg.com/736x/8b/50/ac/8b50ac25d8f51dcddb1fde08154e0785.jpg",
    "https://i.pinimg.com/736x/10/a7/2e/10a72e1112c4cbd2f9324610286abc8c.jpg",
    "https://i.pinimg.com/736x/32/39/bf/3239bf2f1dbb8555976b873ba270e55d.jpg",
    "https://i.pinimg.com/736x/82/a0/c2/82a0c2da2f7ce0dcb5e28b72e34cd2ca.jpg",
    "https://i.pinimg.com/736x/61/b8/48/61b8486787cb4aa1ed4ca581cbbd8012.jpg",
    "https://i.pinimg.com/736x/b9/6c/96/b96c9622476c890b05fd2867fe63b523.jpg",
    "https://i.pinimg.com/736x/f7/78/af/f778afb23abfc1a799ba76b0aa8db4e3.jpg",
    "https://i.pinimg.com/736x/28/49/40/2849401d5057b8ea4bd3835a9cc97bd9.jpg",
    "https://i.pinimg.com/736x/27/01/89/2701899a425bdce1c40f2a74605c6ca8.jpg",
    "https://i.pinimg.com/736x/f5/80/be/f580bed445d19c80484511698785272d.jpg",
    "https://i.pinimg.com/736x/50/70/8a/50708a4fa46a5a53bc8e0b9cb6bc0051.jpg",
    "https://i.pinimg.com/736x/9a/bb/b7/9abbb7828b5645da9ce779b2ab43ea66.jpg",
    "https://i.pinimg.com/736x/3e/4a/c9/3e4ac9403538b6da5922563f9af2fe90.jpg",
    "https://i.pinimg.com/736x/6a/24/52/6a2452cf78f99d50cb5cc9da60fe3efe.jpg",
    "https://i.pinimg.com/736x/9c/82/a1/9c82a1692c3ab7b9e428f57f93d46492.jpg",
    "https://i.pinimg.com/736x/4d/f5/3f/4df53fef71b47bed07cb6207f8738940.jpg",
    "https://i.pinimg.com/736x/2b/c4/ab/2bc4aba5cdd87092c130cc7dd940b36c.jpg",
    "https://i.pinimg.com/736x/55/58/57/55585748d626982a7d3504537f3bead4.jpg",
    "https://i.pinimg.com/736x/96/c6/c7/96c6c7fe144f6d220c5f4d1c40028c02.jpg",
    "https://i.pinimg.com/736x/d4/b9/0d/d4b90d4357cf93c1e10b8a5bd5043acc.jpg",
    "https://i.pinimg.com/736x/b0/e5/32/b0e5328d86789981d4b3d66860806312.jpg",
    "https://i.pinimg.com/736x/c9/6e/3e/c96e3e2f22ef8fb8b16d39eaf764cdfc.jpg",
    "https://i.pinimg.com/736x/d3/08/20/d30820779e1e54b2826a2a0bea63835c.jpg",
    "https://i.pinimg.com/736x/df/0f/6b/df0f6bbecf5f4ddf913dfaf23c18e944.jpg",
    "https://i.pinimg.com/736x/de/c2/46/dec24668d0983645e957b96e497cc0c5.jpg",
    "https://i.pinimg.com/736x/99/ea/0f/99ea0fae51e4a260103881e69a4af253.jpg",
    "https://i.pinimg.com/736x/f4/e1/ce/f4e1ce647fd85c3badc30edfd32342b0.jpg",
    "https://i.pinimg.com/736x/2c/c9/c2/2cc9c22a4bce5dfb642ba8e47aa1fb9d.jpg",
    "https://i.pinimg.com/736x/89/9c/57/899c57c8a331dcf6546ff3bf72754bab.jpg",
    "https://i.pinimg.com/736x/01/ce/d7/01ced7ce5dc8fff7e0d782e53de8db08.jpg",
    "https://i.pinimg.com/736x/03/cd/3a/03cd3a6b588683b57c7aef30dfc35e5b.jpg",
    "https://i.pinimg.com/736x/c2/d9/e0/c2d9e09b7f2c108ff203a6b24bd657d6.jpg",
    "https://i.pinimg.com/736x/da/09/89/da09896e44de7ef9e3412e7931f7517f.jpg",
    "https://i.pinimg.com/736x/f9/cc/f8/f9ccf8a14a6b55fe98745aed43e67a6d.jpg",
    "https://i.pinimg.com/736x/28/75/c2/2875c287386f1fc67997217a74f1560f.jpg",
    "https://i.pinimg.com/736x/07/33/ee/0733ee4b5a56765c5b2060350923c345.jpg",
    "https://i.pinimg.com/736x/0f/b8/23/0fb82360a88fbe8e2e3ac26260c67e3d.jpg",
    "https://i.pinimg.com/736x/bd/5f/c8/bd5fc8ab406a7c50af1fd9ff1a9e4e52.jpg",
    "https://i.pinimg.com/736x/3e/d5/b6/3ed5b63f0c4f6815ec7ba2338a6a36c0.jpg",
    "https://i.pinimg.com/736x/16/3d/85/163d85399f2cb950278cc7c405a2a5b2.jpg",
    "https://i.pinimg.com/736x/79/ce/f7/79cef74deab51be4c9c699ccc4504b1e.jpg",
    "https://i.pinimg.com/736x/5e/86/e5/5e86e545ed2b0411e53d370eb5d9b3e9.jpg",
    "https://i.pinimg.com/736x/1f/76/ea/1f76ead2345e7528e64d1ed129ec13a3.jpg",
    "https://i.pinimg.com/736x/82/09/67/8209676024121f12dc2b92fd6fde4f75.jpg",
    "https://i.pinimg.com/736x/d6/51/ca/d651ca217d59cddc80c1d9903f6e2271.jpg",
    "https://i.pinimg.com/736x/37/38/17/3738176979255aa70eda82fdf4b56684.jpg",
    "https://i.pinimg.com/736x/43/3c/ae/433caec4d885aa3769450fde52e73f86.jpg",
    "https://i.pinimg.com/736x/a3/15/8a/a3158ad1bda6a975a570517a892cfbb6.jpg",
    "https://i.pinimg.com/736x/e1/24/5d/e1245de754c27d49c61a1cb40422a8fc.jpg",
    "https://i.pinimg.com/736x/32/ed/ab/32edab697f3946a064d4700ac7200556.jpg",
    "https://i.pinimg.com/736x/78/9b/73/789b73417b488cc54b6fd4f42197e0ad.jpg",
    "https://i.pinimg.com/736x/67/d0/6f/67d06f7ce72661ea36335b45fbe68b68.jpg",
    "https://i.pinimg.com/736x/69/4f/eb/694feb5782ef7d7c40d37f23b1cd28ef.jpg",
    "https://i.pinimg.com/736x/14/54/ec/1454ec762277fc29e689a0e87d55c09b.jpg",
    "https://i.pinimg.com/736x/35/bd/0a/35bd0a31f060bf86948b798fe53a453b.jpg",
    "https://i.pinimg.com/736x/73/9c/ae/739cae196211d620438cab2abb62e216.jpg",
    "https://i.pinimg.com/736x/55/dd/84/55dd84f0c1e1b16f8cebbe32eaa258e7.jpg",
    "https://i.pinimg.com/736x/47/9f/99/479f99ad1c2c80961039c143546de5a1.jpg",
    "https://i.pinimg.com/736x/e8/c0/b6/e8c0b69bdfef965a35738b8fcc770e81.jpg",
    "https://i.pinimg.com/736x/01/cb/dc/01cbdc702f91c3309676ec634bf1f465.jpg",
    "https://i.pinimg.com/736x/ac/d8/c4/acd8c4984f525a628f4d4fa6cf0ea99f.jpg",
    "https://i.pinimg.com/736x/f8/d6/95/f8d6950722b9239f95d28ad4c932c150.jpg",
    "https://i.pinimg.com/736x/8c/aa/82/8caa820f3cd5f1c39a6829b55dab2593.jpg",
    "https://i.pinimg.com/736x/6a/4f/c4/6a4fc494f0e252361003d3cb32dbf6b1.jpg",
    "https://i.pinimg.com/736x/0e/4c/ce/0e4cce7bdecc2d820aaa8d5857a9a3a9.jpg",
    "https://i.pinimg.com/736x/45/d1/b7/45d1b77ab03bb0a7e0d89469501f29d3.jpg",
    "https://i.pinimg.com/736x/94/2f/c9/942fc9328dd990a9c1b5d41bd7616952.jpg",
    "https://i.pinimg.com/736x/56/a6/63/56a663818a3928c88b6f1fe977428b35.jpg",
    "https://i.pinimg.com/736x/c3/b8/f0/c3b8f0329a115da28dd3b1a2775db879.jpg",
    "https://i.pinimg.com/736x/a1/a8/2b/a1a82bdb7fb84ef29412a7ea8d40c0d0.jpg",
    "https://i.pinimg.com/736x/7a/55/49/7a5549f1417885cf521eb857a044970b.jpg",
    "https://i.pinimg.com/736x/56/37/54/5637545d9412a9f881b5ee97c1bc5467.jpg",
    "https://i.pinimg.com/736x/9d/53/05/9d5305706e0fe101a6d481aff9ef4cce.jpg",
    "https://i.pinimg.com/736x/29/11/ad/2911ad6c13f44d42ba49e107ef56b160.jpg",
    "https://i.pinimg.com/736x/b4/51/68/b451689c1977c1928b3182f84ee1f172.jpg",
    "https://i.pinimg.com/736x/fe/45/4c/fe454c06d1314f6e3748993a787fb96f.jpg",
    "https://i.pinimg.com/736x/3d/06/32/3d06322492fd0c3e7fd90deb272a5eea.jpg",
    "https://i.pinimg.com/736x/1e/9d/43/1e9d430ce8f4689f2aac05d420799e10.jpg",
    "https://i.pinimg.com/736x/f2/8d/b7/f28db7421dc0e9d07a4fe6c4e20030ca.jpg",
    "https://i.pinimg.com/736x/51/2a/62/512a627f3934b202afcf7ae5fc0a8fb4.jpg",
    "https://i.pinimg.com/736x/b3/a7/1c/b3a71c3fb5529c06cc1f02a81ca29dd9.jpg",
    "https://i.pinimg.com/736x/fb/30/b4/fb30b41047a545c48a766910736a23cc.jpg",
    "https://i.pinimg.com/736x/66/f4/d4/66f4d4e1b93b4eeb6066a46c37e4eb7f.jpg",
    "https://i.pinimg.com/736x/cc/ce/c6/cccec6fd37791925bc3f5c6ca7f01f75.jpg",
    "https://i.pinimg.com/736x/30/90/17/3090173306dfef3f0ebd8685798e9d62.jpg",
    "https://i.pinimg.com/736x/4e/cf/49/4ecf492aacc48e4b01447737657e78d2.jpg",
    "https://i.pinimg.com/736x/d4/66/72/d466725014c4909c5f3a23ebfe76c98a.jpg",
    "https://i.pinimg.com/736x/15/61/88/156188a36efb1162f14af5858bee3fb9.jpg",
    "https://i.pinimg.com/736x/df/cb/f3/dfcbf3d0d29cc8038154cf322236a6c5.jpg",
    "https://i.pinimg.com/736x/05/b7/80/05b78000fbba3e0ff4828b9f82ea4293.jpg",
    "https://i.pinimg.com/736x/35/08/0e/35080e6fa5eeb622962466b7df5001c3.jpg",
    "https://i.pinimg.com/736x/f1/9d/7d/f19d7df5f5209d8ce2d251141a373f70.jpg",
    "https://i.pinimg.com/736x/55/6c/ce/556ccef4fdfdafb55dc70e2979382f45.jpg",
    "https://i.pinimg.com/736x/bb/0c/bf/bb0cbf82424ec0b44e21e447df8ea1fd.jpg",
    "https://i.pinimg.com/736x/b9/ec/47/b9ec475ca01df1816e42d8968787d9e2.jpg",
    "https://i.pinimg.com/736x/0c/b7/44/0cb744ea799e3a9f26bb90bf0e81320a.jpg",
    "https://i.pinimg.com/736x/d8/23/30/d823309a7866e67284a419087740c459.jpg",
    "https://i.pinimg.com/736x/45/e3/03/45e303a5da37795d2bf2aebc2720cb07.jpg",
    "https://i.pinimg.com/736x/47/db/50/47db5005ca58bda64eb884225b404c5d.jpg",
    "https://i.pinimg.com/736x/bb/bb/24/bbbb249dac496e67cd296d4b10550007.jpg",
    "https://i.pinimg.com/736x/91/8b/c7/918bc77adcb501ac92e9457a0065239a.jpg",
    "https://i.pinimg.com/736x/67/c5/5b/67c55be0234413081bf683045794729b.jpg",
    "https://i.pinimg.com/736x/a2/39/ab/a239ab3303529190440b643385bbb999.jpg",
    "https://i.pinimg.com/736x/7c/6f/8d/7c6f8d225122ae8abe890a87f4222d05.jpg",
    "https://i.pinimg.com/736x/6d/26/a3/6d26a3f6a2acd7873640d67845d13dd7.jpg",
    "https://i.pinimg.com/736x/81/6e/e9/816ee9ffd51f27431d1a76dd03953d99.jpg",
    "https://i.pinimg.com/736x/d4/b0/d6/d4b0d667e27747bbadfd5e037a9b52d9.jpg",
    "https://i.pinimg.com/736x/0f/92/84/0f9284f0a7a40c4a422342e51d3fe8b9.jpg",
    "https://i.pinimg.com/736x/70/4d/95/704d95b8127a3708f34b097921a9f72b.jpg",
    "https://i.pinimg.com/736x/03/e8/40/03e84073fc1d4cd7ea2a2a06547f09cc.jpg",
    "https://i.pinimg.com/736x/2d/7a/8e/2d7a8e8e0e2a3b5183b5780358641aa6.jpg",
    "https://i.pinimg.com/736x/bf/c8/6d/bfc86d5bf0be5318b07444fa87f86fdb.jpg",
    "https://i.pinimg.com/736x/9c/c4/a8/9cc4a89331962ecc0e809d3a1c9997c6.jpg",
    "https://i.pinimg.com/736x/84/8a/41/848a41ff3957003574ee2fdfc1cf21a4.jpg",
    "https://i.pinimg.com/736x/48/3e/90/483e9040dbfd18b6c1419471e4bd9732.jpg",
    "https://i.pinimg.com/736x/24/c9/55/24c955f754896095a51c3514b45687a1.jpg",
    "https://i.pinimg.com/736x/52/92/38/529238de31f3c82c8320d321021710c5.jpg",
    "https://i.pinimg.com/736x/0b/c1/fe/0bc1fe04c742ec8f59422e9befe619ae.jpg",
    "https://i.pinimg.com/736x/66/c4/b0/66c4b0ab158a8d640058f810efa59314.jpg",
    "https://i.pinimg.com/736x/51/47/00/5147008749efe80ed43eac7ee606e38f.jpg",
    "https://i.pinimg.com/736x/c6/54/11/c654112202337fe5382aef28ea1c897e.jpg",
    "https://i.pinimg.com/736x/70/a8/56/70a8562e749d92b037e994d446a9d075.jpg",
    "https://i.pinimg.com/736x/4b/65/59/4b655900495dc6f63dc7a7a6ce22f52f.jpg",
    "https://i.pinimg.com/736x/f5/86/b9/f586b9fa40f0eb02dca029bc96d6bbb5.jpg",
    "https://i.pinimg.com/736x/85/84/66/8584664541a38dc6528725ef4d8a1336.jpg",
    "https://i.pinimg.com/736x/c3/de/93/c3de93b20946088d80677d2e73344073.jpg",
    "https://i.pinimg.com/736x/ef/f4/69/eff469e8635aec0826972d9871f40298.jpg",
    "https://i.pinimg.com/736x/47/06/c0/4706c0255fd721c58b83762e042e2284.jpg",
    "https://i.pinimg.com/736x/8b/ff/63/8bff6326a2513eb5b43bd02a6a23eb0b.jpg",
    "https://i.pinimg.com/736x/7b/da/e0/7bdae09fd9fe66080eb07933c63e3e68.jpg",
    "https://i.pinimg.com/736x/2c/15/40/2c15409647e74a278cc4301a24e47a2a.jpg",
    "https://i.pinimg.com/736x/d2/fc/38/d2fc387e267b75f808c9bb26e753ec30.jpg",
    "https://i.pinimg.com/736x/ea/db/38/eadb386263aa364d1c7c1fc05e8792be.jpg",
    "https://i.pinimg.com/736x/30/ca/95/30ca9574a8086747752348e225e61c16.jpg",
    "https://i.pinimg.com/736x/4c/07/84/4c07844a8e879fd029bcb919cd482794.jpg",
    "https://i.pinimg.com/736x/72/3e/82/723e82e66afc26cc50ab5fa75cff43f7.jpg",
    "https://i.pinimg.com/736x/87/92/50/87925050634e670a77782b744c015801.jpg",
    "https://i.pinimg.com/736x/8b/30/ca/8b30cabbade483a6af76f0779e32828a.jpg",
    "https://i.pinimg.com/736x/b1/89/98/b18998b775b123b00d16fca31cc8a184.jpg",
    "https://i.pinimg.com/736x/7d/1d/9c/7d1d9c19f93d29f2f8824708fca74a81.jpg",
    "https://i.pinimg.com/736x/04/1a/f5/041af5823fd9e9ac897439cd5e3c9dd2.jpg",
    "https://i.pinimg.com/736x/3d/77/9e/3d779e1b1ef1665744122445369c9aee.jpg",
    "https://i.pinimg.com/736x/ff/e9/8f/ffe98fb89bb590b839e18962fa97d1be.jpg",
    "https://i.pinimg.com/736x/4a/d0/33/4ad0334782e71b6d1862c97c5b9e315b.jpg",
    "https://i.pinimg.com/736x/14/d5/9b/14d59b6568b4cc64c1cd604068134f41.jpg",
    "https://i.pinimg.com/736x/f1/5c/0d/f15c0d9524208c2773bfb6b665bb1e4f.jpg",
    "https://i.pinimg.com/736x/64/f9/ad/64f9adfb0ac8f5d56b679a129a59b286.jpg",
    "https://i.pinimg.com/736x/5d/3d/ca/5d3dca1067a6b6e8c1b3f93df9c641ab.jpg",
    "https://i.pinimg.com/736x/92/9c/f8/929cf854d42ece4ff661c04dd30404f9.jpg",
    "https://i.pinimg.com/736x/13/35/0f/13350fe82dbbf9d0917859386dea6d64.jpg",
    "https://i.pinimg.com/736x/4d/fc/38/4dfc386bb28b70f0e6dbf7d0127c877e.jpg",
    "https://i.pinimg.com/736x/97/d6/94/97d6943b6e240903a6f330f567bf8a99.jpg",
    "https://i.pinimg.com/736x/da/de/f6/dadef6d643cdecb77d774fe2c0fa7e37.jpg",
    "https://i.pinimg.com/736x/ae/d7/26/aed72618223e13e9c81c273df60631fb.jpg",
    "https://i.pinimg.com/736x/c2/50/12/c2501283733f538927383acba8e01218.jpg",
    "https://i.pinimg.com/736x/3c/da/6f/3cda6fe4717708ea10eb2e54c7de315a.jpg",
    "https://i.pinimg.com/736x/af/d8/e9/afd8e90e3542d6f7f6cc978242552813.jpg",
    "https://i.pinimg.com/736x/5e/dd/56/5edd56618d5dff4e17756cb96ea0b37d.jpg",
    "https://i.pinimg.com/736x/c6/d2/b9/c6d2b904c01fd698157767d1f2e9f295.jpg",
    "https://i.pinimg.com/736x/3e/01/b7/3e01b73f652a4f82567c6067c790ea6e.jpg",
    "https://i.pinimg.com/736x/30/c8/53/30c853ad0169db0a4ef1335888575a4c.jpg",
    "https://i.pinimg.com/736x/b2/0b/f6/b20bf6617c97261ccb753a93e7955e60.jpg",
    "https://i.pinimg.com/736x/5a/48/ac/5a48ac57c66e7cf46e435358227eb64c.jpg",
    "https://i.pinimg.com/736x/07/3e/39/073e3938895d631cdc0947487458c33d.jpg",
    "https://i.pinimg.com/736x/50/59/9a/50599a401232d2e3f76227eee356f6f3.jpg",
    "https://i.pinimg.com/736x/45/ab/fa/45abfab9de1b1d1e9bf69d5ad6a8edca.jpg",
    "https://i.pinimg.com/736x/80/8c/f1/808cf1e1b48444ca842a645229484311.jpg",
    "https://i.pinimg.com/736x/dc/40/89/dc4089b4a85e46587f97ba13618b1aa4.jpg",
    "https://i.pinimg.com/736x/bc/10/cd/bc10cdc5183bb4d27382010777d9b3d3.jpg",
    "https://i.pinimg.com/736x/fa/5b/c5/fa5bc52f88d2dc45127c7be3a9e5aa75.jpg",
    "https://i.pinimg.com/736x/cd/15/d0/cd15d0b2b3e54a9fa79cefae2dfd2e9f.jpg",
    "https://i.pinimg.com/736x/a3/63/c1/a363c1e69428e8f83f3bcdb694a34619.jpg",
]

OUT = "public/inspo"
os.makedirs(OUT, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.pinterest.com/",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
}

total = len(URLS)
saved = 0
failed = []

print(f"Downloading {total} nail inspo images to ./{OUT}/")
print("-" * 50)

for i, url in enumerate(URLS, 1):
    fname = f"nail-{i:03d}.jpg"
    dest = os.path.join(OUT, fname)

    # Show progress bar
    pct = i / total
    bar = "█" * int(pct * 30) + "░" * (30 - int(pct * 30))
    sys.stdout.write(f"\r[{bar}] {i}/{total}  ")
    sys.stdout.flush()

    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        saved += 1
    except Exception as e:
        failed.append((fname, str(e)))

    time.sleep(0.08)  # gentle rate limiting

print(f"\n\n✅ Done! {saved} images saved to ./{OUT}/")
if failed:
    print(f"⚠️  {len(failed)} failed:")
    for name, err in failed:
        print(f"   {name}: {err}")
