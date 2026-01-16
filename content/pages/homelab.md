Title: Gear / Homelab
Subtitle: Daily Drivers · Self-Hosted Services · Network Topology
Slug: homelab
Modified: 2026-01-16

## Computing

<div class="computing-compact">
  <div>
    <h3>neo@box</h3>
    <ul>
      <li>Ryzen 7 3700X</li>
      <li>GTX 1650</li>
      <li>64GB RAM</li>
      <li>CachyOS · Hyprland</li>
    </ul>
  </div>
  <div>
    <h3>ThinkPad T14p gen2</h3>
    <ul>
      <li>Some AMD CPU</li>
      <li>48GB RAM</li>
      <li>Project Bluefin · Gnome</li>
    </ul>
  </div>
</div>

<div class="homelab-section">
<h2>Homelab Infrastructure</h2>

<a href="{static}/images/lab.jpg" target="_blank" class="lab-photo-inline">
  <img src="{static}/images/lab.jpg" alt="Server rack" style="display: block; max-width: 100%;">
</a>

<h3>Hardware</h3>

<strong>Servers & Network</strong>
<ul>
  <li>ZimaBlade NAS <span class="meta">[tiny] 2×1TB mirror</span></li>
  <li>ThinkCentre fleet [x3] <span class="meta">VMs · Docker · HA</span></li>
  <li>Hetzner Dedicated Server <span class="meta">Ryzen 3700X · 64GB</span></li>
  <li>Ubiquiti ERPoE-5</li>
  <li>Ubiquiti U6 Lite APs</li>
  <li>Netgear switches</li>
</ul>

<h3>Services</h3>

<div class="services-grid">
  <div>
    <h4>Home VMs</h4>
    <ul>
      <li>TrueNAS SCALE</li>
      <li>Proxmox Backup Server</li>
      <li>Prometheus/Grafana</li>
      <li>DNS/DHCP/AdGuard</li>
      <li>Development ENV VMs</li>
    </ul>
  </div>
  <div>
    <h4>Datacenter VMs</h4>
    <ul>
      <li>Jellyfin</li>
      <li>Remote NAS</li>
      <li>Monitoring stack</li>
    </ul>
  </div>
  <div>
    <h4>Containers</h4>
    <ul>
      <li>Home Assistant, Frigate</li>
      <li>Gitea, Miniflux</li>
      <li>Komodo, Memos, Lychee</li>
      <li>Pi-hole, MQTT, InfluxDB</li>
      <li>Caddy, Grafana</li>
    </ul>
  </div>
  <div>
    <h4>Utilities</h4>
    <ul>
      <li>Solidtime</li>
      <li>Karakeep</li>
      <li>Unifi Controller</li>
      <li>Encrypted text sharing</li>
    </ul>
  </div>
</div>

<h3>Architecture</h3>

<p>Site-to-site WireGuard VPN links home network to Hetzner datacenter. Primary host scrapstack-0 serves as WireGuard endpoint and reverse proxy for LAN access. Hetzner runs Proxmox with ZFS mirror on HDDs. EdgeRouter handles static routes. Services split between Docker containers at home and Proxmox VMs at both sites for redundancy during internet outages or datacenter maintenance.</p>

</div>

## Hobbies

<div class="hobbies-grid">
  <div>
    <h3>Photography</h3>
    <h4>Digital</h4>
    <ul>
      <li>Fujifilm X-Pro2 <span class="meta">26MP APS-C</span></li>
      <li>Fujinon XF 16-80mm f/4 <span class="meta">OIS WR</span></li>
      <li>TTartisan 27mm f/2.8</li>
      <li>Viltrox 33mm f/1.4</li>
    </ul>
    <h4>Analog</h4>
    <ul>
      <li>Pentax ME <span class="meta">35mm Film</span></li>
      <li>SMC Pentax-M 50mm f/1.4</li>
      <li>SMC Pentax-M 28mm f/2.8</li>
      <li>Helios 44-2 58mm f/2 <span class="meta">M42</span></li>
    </ul>
  </div>

  <div>
    <h3>Audio</h3>
    <h4>Source & Amplification</h4>
    <ul>
      <li>Fisher MT-6321 <span class="meta">Turntable</span></li>
      <li>JVC XL-V221BK <span class="meta">CD Player</span></li>
      <li>Onkyo A-8670 <span class="meta">Integrated Amp</span></li>
    </ul>
    <h4>Output</h4>
    <ul>
      <li>Polk RTi A3 <span class="meta">Bookshelf</span></li>
      <li>Arcus TM-65 <span class="meta">Speakers</span></li>
      <li>Hifiman Sundara <span class="meta">Planar</span></li>
      <li>Sennheiser HD598 <span class="meta">Open-back</span></li>
      <li>Shure SE215 <span class="meta">IEMs</span></li>
    </ul>
  </div>

  <div>
    <h3>3D Printing</h3>
    <ul>
      <li>Prusa Mini+ <span class="meta">FDM · 180×180×180mm</span></li>
      <li>Prusa Mk3s+ <span class="meta">FDM · 250×210×210mm</span></li>
      <li>PrusaSlicer <span class="meta">Slicing software</span></li>
      <li>Materials: PLA, PETG, TPU</li>
      <li>Prints: Functional parts, enclosures, tooling, prototypes</li>
    </ul>
  </div>

  <div>
    <h3>Sim Racing</h3>
    <img src="{static}/images/carsim.png" alt="Sim racing rig">
    <ul>
      <li>BMW E36 Interior <span class="meta">E39 Seat</span></li>
      <li>Moza Racing Shifter</li>
      <li>Logitech G923 <span class="meta">Wheel & Pedals</span></li>
      <li>LG Ultrawide <span class="meta">1440p</span></li>
      <li>AMD Ryzen 7 2700 + GTX 2070</li>
    </ul>
  </div>
</div>
