<script setup>
import { ref, onMounted } from 'vue'

// Reaktiní proměnné pro stav systému
const myslitele = ref([])
const nacteno = ref(false)
const chyba = ref(null)

// Funkce pro načtení dat z Django API
const nactiData = async () => {
  try {
    const response = await fetch('http://127.0.0.1:10000/api/myslitele')
    if (!response.ok) throw new Error('Chyba při komunikaci s ontologickým jádrem.')
    myslitele.value = await response.json()
  } catch (err) {
    chyba.value = err.message
  } finally {
    nacteno.value = true
  }
}

// Spustí se při inicializaci komponenty
onMounted(() => {
  nactiData()
})
</script>

<template>
  <div class="obsidian-app">
    <div class="noise-overlay"></div>

    <header class="monumental-header">
      <div class="logo">I.D.E.A. <span class="accent">INSTITUT</span></div>
      <nav class="sleek-nav">
        <a href="#" class="nav-link">ARCHIV</a>
        <a href="#" class="nav-link">PROUD</a>
        <a href="#" class="nav-link">ONTOLOGIE</a>
      </nav>
    </header>

    <main class="hero-section">
      <div class="title-container">
        <h1 class="main-title">Panteon <br/><span class="glow">Absolutna</span></h1>
        <p class="subtitle">Interaktivní brána do hlubin lidského logu. Vyberte titána a studujte kód reality.</p>
      </div>

      <div v-if="!nacteno" class="status-message">
        <span class="loading-pulse">Inicializace synchronizace dat...</span>
      </div>

      <div v-else-if="chyba" class="status-message error">
        Kritická chyba: {{ chyba }}
      </div>

      <div v-else class="philosopher-grid">
        <div v-for="myslitel in myslitele" :key="myslitel.id" class="monolith-card">
          <div class="card-inner">
            <div class="portrait-placeholder">
              <span class="initials">{{ myslitel.inicialy }}</span>
            </div>
            <div class="card-content">
              <h3>{{ myslitel.jmeno }}</h3>
              <p class="era">{{ myslitel.epocha }}</p>
              <div class="quote-preview">„{{ myslitel.citat }}“</div>
              <button class="detail-btn">VSTOUPIT DO MYSLI</button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="obsidian-footer">
      <p>MATOUŠ TLAMKA — I.D.E.A. 2026 — <a href="https://matous-tlamka.eu">SYSTEM ONLINE</a></p>
    </footer>
  </div>
</template>

<style>
:root {
  --orange: #ff6600;
  --black: #000000;
  --obsidian: #0a0a0a;
  --text: #e0e0e0;
  --gray: #8a8a8a;
}

body {
  margin: 0;
  font-family: 'Montserrat', sans-serif;
  color: var(--text);
  background: var(--black);
  overflow-x: hidden;
}

.obsidian-app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.noise-overlay {
  position: fixed;
  inset: 0;
  background: url('https://grainy-gradients.vercel.app/noise.svg');
  opacity: 0.05;
  pointer-events: none;
  z-index: 999;
}

.monumental-header {
  padding: 40px 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255,102,0,0.1);
}

.logo {
  font-family: 'Playfair Display', serif;
  font-size: 1.8rem;
  letter-spacing: 5px;
}

.accent { color: var(--orange); }

.sleek-nav { display: flex; gap: 40px; }
.nav-link {
  text-decoration: none;
  color: var(--text);
  font-size: 0.8rem;
  letter-spacing: 3px;
  transition: 0.3s;
}

.nav-link:hover { color: var(--orange); }

.hero-section {
  padding: 100px 60px;
  flex-grow: 1;
}

.main-title {
  font-family: 'Playfair Display', serif;
  font-size: 8rem;
  margin: 0;
  line-height: 0.9;
  text-transform: uppercase;
}

.glow {
  color: var(--orange);
  text-shadow: 0 0 30px rgba(255, 102, 0, 0.4);
}

.subtitle {
  font-size: 1.2rem;
  color: var(--gray);
  max-width: 600px;
  margin: 40px 0;
}

/* STAVY NAČÍTÁNÍ */
.status-message {
  margin-top: 80px;
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  color: var(--gray);
}
.error { color: #ff3333; }
.loading-pulse { animation: pulse 1.5s infinite; }
@keyframes pulse {
  0% { opacity: 0.5; }
  50% { opacity: 1; color: var(--orange); }
  100% { opacity: 0.5; }
}

/* PHILOSOPHER GRID */
.philosopher-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 30px;
  margin-top: 80px;
}

.monolith-card {
  background: var(--obsidian);
  border: 1px solid #1a1a1a;
  height: 500px;
  position: relative;
  transition: 0.6s cubic-bezier(0.23, 1, 0.32, 1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.monolith-card:hover {
  border-color: var(--orange);
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(255,102,0,0.1);
}

.portrait-placeholder {
  height: 250px;
  background: #050505;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid #1a1a1a;
}

.initials {
  font-family: 'Playfair Display', serif;
  font-size: 5rem;
  color: #1a1a1a;
  transition: 0.4s;
}

.monolith-card:hover .initials {
  color: var(--orange);
  text-shadow: 0 0 20px rgba(255,102,0,0.5);
}

.card-content { padding: 30px; flex-grow: 1; display: flex; flex-direction: column; }
.card-content h3 { margin: 0; font-size: 1.5rem; letter-spacing: 1px; color: var(--text); }
.era { color: var(--orange); font-size: 0.7rem; text-transform: uppercase; margin-top: 5px; }
.quote-preview { margin-top: 20px; font-style: italic; color: var(--gray); font-size: 0.95rem; }

.detail-btn {
  margin-top: auto;
  background: none;
  border: 1px solid var(--orange);
  color: var(--orange);
  padding: 10px 20px;
  cursor: pointer;
  font-family: 'Montserrat';
  letter-spacing: 2px;
  transition: 0.3s;
  align-self: flex-start;
}

.detail-btn:hover {
  background: var(--orange);
  color: #000;
}

.obsidian-footer {
  padding: 40px;
  text-align: center;
  border-top: 1px solid #1a1a1a;
  font-size: 0.7rem;
  letter-spacing: 2px;
  color: var(--gray);
}
</style>