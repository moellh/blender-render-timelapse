<template>
  <div v-if="$slidev.nav.currentPage !== 1" class="slide-number-container">
    <SlideCurrentNo />
  </div>
</template>

<style>
.slide-number-container {
  position: fixed;
  bottom: 1.2rem;
  right: 1.5rem;
  font-size: 0.75rem;
  font-family: 'JetBrains Mono', monospace;
  opacity: 0.4;
  pointer-events: none;
  z-index: 100;
  color: inherit;
}
</style>
