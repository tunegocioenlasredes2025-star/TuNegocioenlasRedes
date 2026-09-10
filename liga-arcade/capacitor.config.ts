import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'ar.tunegocioenlasredes.ligaarcade',
  appName: 'Liga Arcade',
  webDir: 'www',
  android: {
    allowMixedContent: false,
    backgroundColor: '#0b1d0f',
  },
  server: { androidScheme: 'https' },
};

export default config;
