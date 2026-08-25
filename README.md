<style>
  .profile-card {
    background: linear-gradient(135deg, #0d0221 0%, #1a0a3e 50%, #0d0221 100%);
    border: 1px solid rgba(168, 85, 247, 0.3);
    border-radius: 12px;
    padding: 2rem;
    margin: 1rem 0;
  }
  .profile-card h2 {
    color: #c084fc;
    font-size: 1.4rem;
    margin-top: 0;
  }
  .profile-card p {
    color: #a3a3a3;
    line-height: 1.6;
  }
  .tag {
    display: inline-block;
    background: rgba(168, 85, 247, 0.15);
    color: #c084fc;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    margin: 4px;
    border: 1px solid rgba(168, 85, 247, 0.3);
  }
  .skill-bar {
    height: 6px;
    border-radius: 3px;
    background: rgba(255,255,255,0.08);
    margin: 8px 0;
    overflow: hidden;
  }
  .skill-fill {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, #6d28d9, #a855f7);
  }
  .project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem;
  }
  .project-item {
    background: linear-gradient(135deg, rgba(109, 40, 217, 0.08), rgba(168, 85, 247, 0.04));
    border: 1px solid rgba(168, 85, 247, 0.15);
    border-radius: 10px;
    padding: 1.2rem;
    transition: border-color 0.2s;
  }
  .project-item:hover {
    border-color: rgba(168, 85, 247, 0.5);
  }
  .project-item h3 {
    color: #e9d5ff;
    margin: 0 0 0.4rem;
    font-size: 1rem;
  }
  .project-item p {
    color: #737373;
    margin: 0;
    font-size: 0.85rem;
    line-height: 1.5;
  }
  .project-item .tech {
    color: #a78bfa;
    font-size: 0.75rem;
    margin-top: 0.5rem;
  }
  .nova-card {
    background: linear-gradient(135deg, #1e0a3c 0%, #2d1065 50%, #1a0a3e 100%);
    border: 1px solid rgba(168, 85, 247, 0.4);
    border-radius: 14px;
    padding: 2rem;
    margin: 1.5rem 0;
    position: relative;
    overflow: hidden;
  }
  .nova-card::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(168, 85, 247, 0.06) 0%, transparent 70%);
    pointer-events: none;
  }
  .nova-card h2 {
    color: #e9d5ff;
    font-size: 1.6rem;
    margin-top: 0;
    position: relative;
  }
  .nova-card p {
    color: #a3a3a3;
    line-height: 1.7;
    position: relative;
  }
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(168, 85, 247, 0.3), transparent);
    margin: 2.5rem 0;
  }
  .section-title {
    color: #c084fc;
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(168, 85, 247, 0.3), transparent);
  }
  .tech-pill {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    margin: 3px;
    color: #d4d4d4;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
  }
</style>

<div align="center">
  <svg width="600" height="160" viewBox="0 0 600 160" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#c084fc"/>
        <stop offset="50%" stop-color="#a855f7"/>
        <stop offset="100%" stop-color="#7c3aed"/>
      </linearGradient>
      <linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#c084fc" stop-opacity="0"/>
        <stop offset="30%" stop-color="#c084fc" stop-opacity="0.4"/>
        <stop offset="70%" stop-color="#a855f7" stop-opacity="0.4"/>
        <stop offset="100%" stop-color="#a855f7" stop-opacity="0"/>
      </linearGradient>
      <filter id="glow">
        <feGaussianBlur stdDeviation="2" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <line x1="0" y1="30" x2="600" y2="30" stroke="url(#g2)" stroke-width="1"/>
    <line x1="0" y1="130" x2="600" y2="130" stroke="url(#g2)" stroke-width="1"/>
    <text x="300" y="75" text-anchor="middle" font-family="monospace" font-size="38" font-weight="bold" fill="url(#g1)" filter="url(#glow)">MrNova420</text>
    <text x="300" y="105" text-anchor="middle" font-family="monospace" font-size="13" fill="#7c7c7c">Ecosystem Builder · 150+ Projects · 20+ Languages</text>
    <circle cx="80" cy="30" r="2" fill="#c084fc" opacity="0.6"/>
    <circle cx="520" cy="30" r="2" fill="#a855f7" opacity="0.6"/>
    <circle cx="80" cy="130" r="2" fill="#a855f7" opacity="0.6"/>
    <circle cx="520" cy="130" r="2" fill="#c084fc" opacity="0.6"/>
  </svg>
</div>

<div align="center">
  <span class="tag">🎮 Game Engines</span>
  <span class="tag">🧠 AI Systems</span>
  <span class="tag">🛡️ Security</span>
  <span class="tag">🔧 Reverse Engineering</span>
  <span class="tag">🌐 Web Platforms</span>
  <span class="tag">⚙️ Automation</span>
</div>

<div class="divider"></div>

## About

> *"I'm a developer focused on long-term projects and experimentation — all repositories are under active development and continuously improved."*

I don't build apps. I build **platforms**. Game engines from scratch in C++. AI agents that control your entire computer. Cybersecurity suites with thousands of passing tests. Browser-based world editors rivaling desktop tools. Entire game industry stacks — engine, editor, store — built solo, continuously evolving.

<div class="divider"></div>

## 👑 NovaForge

<div class="nova-card">
  <h2>The 3-in-1 Game Platform</h2>
  <p>Not a framework. Not a library. A <strong>complete game industry stack</strong> built from scratch.</p>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; margin-top: 1.5rem; position: relative;">
    <div style="background: rgba(168,85,247,0.08); border-radius: 8px; padding: 1rem;">
      <div style="color: #e9d5ff; font-weight: 600; margin-bottom: 0.4rem;">🧬 NovaCore</div>
      <div style="color: #737373; font-size: 0.85rem;">Custom AAA game engine built from scratch in <strong style="color: #c084fc;">C++23</strong> with Vulkan rendering</div>
    </div>
    <div style="background: rgba(168,85,247,0.08); border-radius: 8px; padding: 1rem;">
      <div style="color: #e9d5ff; font-weight: 600; margin-bottom: 0.4rem;">🛠️ Editor</div>
      <div style="color: #737373; font-size: 0.85rem;">Native game development tools — build on real devices with a Vulkan pipeline</div>
    </div>
    <div style="background: rgba(168,85,247,0.08); border-radius: 8px; padding: 1rem;">
      <div style="color: #e9d5ff; font-weight: 600; margin-bottom: 0.4rem;">🕹️ Store</div>
      <div style="color: #737373; font-size: 0.85rem;">Game library & store — publish your creations, players discover and play</div>
    </div>
  </div>
</div>

<div class="divider"></div>

## Flagships

<div class="project-grid">
  <div class="project-item">
    <h3>🔥 Nova-Forge</h3>
    <p>3-in-1 game platform — custom engine + editor + store</p>
    <div class="tech">C++23 · Vulkan · Python</div>
  </div>
  <div class="project-item">
    <h3>🌍 NovaForge World Engine</h3>
    <p>Browser-based AAA world editor — terrain, forests, export to any engine</p>
    <div class="tech">TypeScript · Three.js · WebGPU</div>
  </div>
  <div class="project-item">
    <h3>🧩 WebForge</h3>
    <p>Web game dev platform — 227 source files, feature-complete</p>
    <div class="tech">TypeScript · 1,910 tests</div>
  </div>
  <div class="project-item">
    <h3>🤖 Varro</h3>
    <p>100% local autonomous AI developer — 9 agents, 28 tools, zero cloud</p>
    <div class="tech">Python · 1,059 tests</div>
  </div>
  <div class="project-item">
    <h3>🗣️ Nexus</h3>
    <p>Multimodal voice AI — sees, hears, controls your computer</p>
    <div class="tech">Gemini 2.5 Live API</div>
  </div>
  <div class="project-item">
    <h3>🧠 RoyalOS</h3>
    <p>Self-hostable AI operating platform — agent fleet control plane</p>
    <div class="tech">TypeScript</div>
  </div>
  <div class="project-item">
    <h3>🛡️ <a href="https://github.com/MrNova420/RoyalSecurity" style="color: #c084fc;">RoyalSecurity</a></h3>
    <p>Open-source EDR/XDR/SIEM — all-in-one cybersecurity in a single agent</p>
    <div class="tech">Rust · Tauri 2 · Next.js 16</div>
  </div>
  <div class="project-item">
    <h3>🧬 BLOCKLIFE-AI</h3>
    <p>Living Minecraft civilization engine — quantized local models</p>
    <div class="tech">TypeScript · Ollama</div>
  </div>
  <div class="project-item">
    <h3>🌌 Aetheria</h3>
    <p>Browser RPG — 255 procedural galaxies, GTA × No Man's Sky</p>
    <div class="tech">Three.js · WebGL2</div>
  </div>
  <div class="project-item">
    <h3>💀 NEON ARENA</h3>
    <p>Cyberpunk FPS — AI bots, multiplayer, neon aesthetics</p>
    <div class="tech">TypeScript · 750+ tests</div>
  </div>
  <div class="project-item">
    <h3>🔍 AutoOffsetDumper</h3>
    <p>Universal memory-offset scanner — 25+ engines, ML classification</p>
    <div class="tech">Rust · C#</div>
  </div>
  <div class="project-item">
    <h3>👁️ omnieye</h3>
    <p>RF/network reconnaissance — 6 collectors, 3D web UI</p>
    <div class="tech">Python</div>
  </div>
  <div class="project-item">
    <h3>🔐 DNALockOS</h3>
    <p>DNA-key authentication — commercial-grade security</p>
    <div class="tech">Python</div>
  </div>
  <div class="project-item">
    <h3>🖥️ <a href="https://github.com/MrNova420/AnVPS" style="color: #c084fc;">AnVPS</a></h3>
    <p>Android → hardened VPS — runs on 32MB RAM, auto-healing</p>
    <div class="tech">Shell</div>
  </div>
  <div class="project-item">
    <h3>⚡ odysseus</h3>
    <p>Self-hosted AI workspace — agents, MCP, memory, privacy-first</p>
    <div class="tech">JavaScript</div>
  </div>
</div>

<div class="divider"></div>

## Project Vault

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">

<div>

<div class="section-title">🎮 Game Engines & Worlds</div>

<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>NovaForge World Engine</h3>
  <p>Browser-based AAA world editor with Three.js + WebGPU</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>WebForge</h3>
  <p>Full web game dev platform — UE5-quality rendering, Unity-ease workflow</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>Aetheria: Endless Frontiers</h3>
  <p>8.4 billion star systems per galaxy, seamless exploration</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>NEON ARENA</h3>
  <p>Cyberpunk FPS with AI bots and multiplayer</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>procedural-sprite-factory</h3>
  <p>Automated sprite generation pipeline</p>
</div>

<div class="section-title">🧠 AI Systems</div>

<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>Nexus</h3>
  <p>Multimodal voice assistant — screen analysis, workflow automation</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>Varro</h3>
  <p>Autonomous developer that learns your codebase and style</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>RoyalOS</h3>
  <p>AI workspace, Discord communities, agent fleets — one dashboard</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>BLOCKLIFE-AI</h3>
  <p>Self-aware Minecraft civilization running locally via Ollama</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>odysseus</h3>
  <p>Self-hosted workspace — vLLM, llama.cpp, Ollama, MCP + memory</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>AINeralNet</h3>
  <p>Centralized multi-model AI secured by DNA-key auth</p>
</div>

</div>
<div>

<div class="section-title">🛡️ Security & Defense</div>

<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3><a href="https://github.com/MrNova420/RoyalSecurity" style="color: #c084fc;">RoyalSecurity</a></h3>
  <p>Open-source EDR/XDR/SIEM/HIPS/DLP — Rust + Tauri + Next.js</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>DNALockOS</h3>
  <p>Proprietary DNA-key authentication system</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>omnieye</h3>
  <p>Phone-based RF/network recon — 6 collectors, 3D UI, no root</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>JARVIS-Cybersecurity</h3>
  <p>Full-stack security platform with real-time scanning</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>innerflect</h3>
  <p>Secure, anonymous, self-healing public website</p>
</div>

<div class="section-title">🔬 Reverse Engineering</div>

<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>AutoOffsetDumper</h3>
  <p>Universal memory-offset scanner — 25+ engines, ML + LLM</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>Nova-BioRadar</h3>
  <p>Android life-form detection radar — Kotlin, 18k lines</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>PHANTOM</h3>
  <p>Tactical network overlay module</p>
</div>

<div class="section-title">📱 Infrastructure</div>

<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3><a href="https://github.com/MrNova420/AnVPS" style="color: #c084fc;">AnVPS</a></h3>
  <p>Android → hardened VPS, 32MB RAM, one-command install</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3><a href="https://github.com/MrNova420/WinVPS" style="color: #c084fc;">WinVPS</a></h3>
  <p>Windows fork of AnVPS</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>NeuralMesh</h3>
  <p>Infrastructure orchestration — any device → server node</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>minecraft-server-manager</h3>
  <p>Android device → 24/7 MC server</p>
</div>

<div class="section-title">⛏️ Automation</div>

<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>Verus Miner Fleet</h3>
  <p>12+ automated mining tools, pool switching, full automation</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>li-li-viral-farm</h3>
  <p>Autonomous multi-account social media farm</p>
</div>

<div class="section-title">🕹️ Game Automation</div>

<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>Civilization-MC-Bots</h3>
  <p>Autonomous bots building civilizations in Minecraft</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>AFK-McBot Series</h3>
  <p>V1 → V2 → V3 → Stable, servers alive 24/7</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3><a href="https://github.com/MrNova420/minefind" style="color: #c084fc;">minefind</a></h3>
  <p>Rust-powered Minecraft server discovery</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3><a href="https://github.com/MrNova420/ScriptVaultLibs" style="color: #c084fc;">ScriptVaultLibs</a></h3>
  <p>Lua library suite — UI, utils, core frameworks</p>
</div>

<div class="section-title">🧬 NovaForge Family</div>

<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>Nova-Forge</h3>
  <p>3-in-1: NovaCore C++23 engine + editor + store</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>NovaForge World Engine</h3>
  <p>Browser AAA editor — terrain sculpting + forest painting</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>NovaCore Engine</h3>
  <p>Custom engine from scratch — Vulkan rendering pipeline</p>
</div>
<div class="project-item" style="margin-bottom: 0.8rem;">
  <h3>royal-forge</h3>
  <p>Royal Commander task manager CLI in Rust</p>
</div>

</div>
</div>

<div class="divider"></div>

## Blueprints

<div class="profile-card">
  <h2>Planned Architecture</h2>
  <p>Every system has a blueprint. These are the long-term visions:</p>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
    <div>
      <div style="color: #e9d5ff; font-weight: 600;">Nova-Forge</div>
      <div style="color: #737373; font-size: 0.85rem;">NovaCore engine (C++23) + device editor (Vulkan) + game store app</div>
    </div>
    <div>
      <div style="color: #e9d5ff; font-weight: 600;">RoyalOS</div>
      <div style="color: #737373; font-size: 0.85rem;">Agent creation, workflows, voice, multi-model routing, extension ecosystem</div>
    </div>
    <div>
      <div style="color: #e9d5ff; font-weight: 600;">WebForge</div>
      <div style="color: #737373; font-size: 0.85rem;">"Unreal-quality rendering, Unity-ease workflow, Blender-class modeling"</div>
    </div>
    <div>
      <div style="color: #e9d5ff; font-weight: 600;">Aetheria</div>
      <div style="color: #737373; font-size: 0.85rem;">255 procedural galaxies, factions, loot, floating islands, corrupted biomes</div>
    </div>
    <div>
      <div style="color: #e9d5ff; font-weight: 600;">Nexus</div>
      <div style="color: #737373; font-size: 0.85rem;">"The bridge between you and your digital environment"</div>
    </div>
    <div>
      <div style="color: #e9d5ff; font-weight: 600;">BLOCKLIFE</div>
      <div style="color: #737373; font-size: 0.85rem;">Bedrock → Java → cross-play, one model running a self-aware civilization</div>
    </div>
  </div>
</div>

<div class="divider"></div>

## Focus

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem;">

<div class="profile-card">
  <h2>🔧 Reverse Engineering</h2>
  <p>Binary analysis, memory scanning, offset dumping, low-level tooling</p>
</div>
<div class="profile-card">
  <h2>🛡️ Security Research</h2>
  <p>Exploit development & vulnerability discovery</p>
</div>
<div class="profile-card">
  <h2>🫥 Evasion Research</h2>
  <p>Protection/detection bypass techniques, anti-cheat analysis</p>
</div>
<div class="profile-card">
  <h2>🌐 Web Building</h2>
  <p>Full-stack sites, platforms & app ecosystems</p>
</div>
<div class="profile-card">
  <h2>🤖 Game Automation</h2>
  <p>Bot frameworks & scripting across game platforms</p>
</div>
<div class="profile-card">
  <h2>🧠 AI Agents</h2>
  <p>Local models, autonomous dev assistants, agent fleets</p>
</div>

</div>

<div class="divider"></div>

## Stack

<div align="center">
  <span class="tech-pill">Python</span>
  <span class="tech-pill">JavaScript</span>
  <span class="tech-pill">TypeScript</span>
  <span class="tech-pill">Rust</span>
  <span class="tech-pill">C#</span>
  <span class="tech-pill">C++</span>
  <span class="tech-pill">Lua</span>
  <span class="tech-pill">Luau</span>
  <span class="tech-pill">Shell</span>
  <span class="tech-pill">PowerShell</span>
  <span class="tech-pill">Kotlin</span>
  <span class="tech-pill">SQL</span>
  <span class="tech-pill">HTML/CSS</span>
  <span class="tech-pill">GLSL</span>
  <span class="tech-pill">WASM</span>
  <br/>
  <span class="tech-pill">Three.js</span>
  <span class="tech-pill">WebGL2</span>
  <span class="tech-pill">WebGPU</span>
  <span class="tech-pill">Next.js</span>
  <span class="tech-pill">React</span>
  <span class="tech-pill">Tauri</span>
  <span class="tech-pill">Node.js</span>
  <span class="tech-pill">Vulkan</span>
  <br/>
  <span class="tech-pill">Ollama</span>
  <span class="tech-pill">Gemini API</span>
  <span class="tech-pill">Git</span>
  <span class="tech-pill">Docker</span>
  <span class="tech-pill">CMake</span>
  <span class="tech-pill">Jetpack Compose</span>
</div>

<div class="divider"></div>

## Currently Building

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
  <div class="project-item">
    <h3>🧬 NovaCore engine</h3>
    <p>Custom AAA game engine from scratch in C++23 with Vulkan</p>
  </div>
  <div class="project-item">
    <h3>🔍 Memory-analysis tooling</h3>
    <p>Rust rewrite, ML-assisted classification</p>
  </div>
  <div class="project-item">
    <h3>🔐 Encrypted delivery platform</h3>
    <p>Offline-first protection system</p>
  </div>
  <div class="project-item">
    <h3>🤖 Agent platform expansion</h3>
    <p>Fleet management, voice, community systems</p>
  </div>
  <div class="project-item">
    <h3>🎬 Movie stream pipeline</h3>
    <p>Sniffer → downloader → player</p>
  </div>
  <div class="project-item">
    <h3>🌍 Procedural world generation</h3>
    <p>Luau-based map systems for Roblox Studio</p>
  </div>
</div>

<div class="divider"></div>

## Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=MrNova420&show_icons=true&hide_border=true&bg_color=0D1117&title_color=A855F7&icon_color=C084FC&text_color=E6EDF3&border_color=21262d" height="165" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=MrNova420&layout=compact&hide_border=true&bg_color=0D1117&title_color=A855F7&text_color=E6EDF3&langs_count=10&border_color=21262d" height="165" />
  <br/>
  <img src="https://streak-stats.demolab.com?user=MrNova420&hide_border=true&background=0D1117&stroke=A855F7&ring=C084FC&fire=F472B6&currStreakLabel=A855F7&sideLabels=E6EDF3&dates=8B949E&border=21262d" height="165" />
  <br/>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=MrNova420&bg_color=0D1117&color=E6EDF3&line=A855F7&point=C084FC&hide_border=true&area=true&area_color=6D28D9&border_color=21262d" width="100%" />
  <br/>
  <img src="https://github-profile-trophy.vercel.app/?username=MrNova420&theme=radical&no-frame=true&row=1&column=7&margin-w=8" width="100%" />
</div>

<div class="divider"></div>

## Snake

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/snake-light.svg" />
  <img alt="Animated snake eating through the contribution grid" src="assets/snake-dark.svg" width="100%" />
</picture>
</div>

<div class="divider"></div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=80&section=footer&color=0:6d28d9,100:a855f7" width="100%" />
  <br/>
  <span style="color: #7c7c7c; font-family: monospace;">MrNova420 · WeNova Interactive</span>
  <br/>
  <span style="color: #525252; font-family: monospace; font-size: 0.8rem;">All repositories under active development and continuously improved.</span>
</div>
