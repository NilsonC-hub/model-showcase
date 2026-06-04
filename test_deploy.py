import urllib.request

base = 'https://nilsonc-hub.github.io/model-showcase/'

# Test index.html
req = urllib.request.Request(base)
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')
print('Index:', resp.status, 'size:', len(html), 'bytes')
print('Has cards:', '.card' in html)
print('Card count:', html.count('class="card"'))

# Test GLB file
glb_url = base + '模型GLB_optimized/web/赛博忍者.glb'
req2 = urllib.request.Request(glb_url)
resp2 = urllib.request.urlopen(req2)
glb_data = resp2.read()
print('GLB:', resp2.status, 'size:', round(len(glb_data)/1024/1024, 2), 'MB')

# Test draco
draco_url = base + 'draco/draco_decoder.js'
req3 = urllib.request.Request(draco_url)
resp3 = urllib.request.urlopen(req3)
print('Draco:', resp3.status, 'size:', len(resp3.read()), 'bytes')

# Test model-showcase-v2.html
v2_url = base + 'model-showcase-v2.html'
req4 = urllib.request.Request(v2_url)
resp4 = urllib.request.urlopen(req4)
v2_html = resp4.read().decode('utf-8')
print('V2 page:', resp4.status, 'has model-viewer:', 'model-viewer' in v2_html)

print()
print('All tests passed!')
