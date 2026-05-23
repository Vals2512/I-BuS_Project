import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-dashboard',
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss',
})
export class Dashboard {
  altoContraste = true;
  modoOscuro = true;
  notificaciones = true;
  tamanoTexto = 50; // valor del slider

  favoritos = [
    { tipo: 'casa', nombre: 'Casa', direccion: 'Calle 10 # 5-20' },
    { tipo: 'trabajo', nombre: 'Trabajo', direccion: 'Avenida El Dorado # 60-15' },
    { tipo: 'trabajo', nombre: 'Universidad', direccion: 'Carrera 30 # 45-03' },
    { tipo: 'casa', nombre: 'Casa de Abuela', direccion: 'Transversal 5 # 78-12' }
  ];

  historial = [
    { ruta: 'Ruta 1 - Circular Norte', tiempo: 'Hace 5 min' },
    { ruta: 'Ruta 5 - Expreso Sur', tiempo: 'Ayer' },
    { ruta: 'Ruta 10 - Transversal', tiempo: 'Hace 3 días' },
    { ruta: 'Ruta 3 - Alimentador', tiempo: 'Hace 1 semana' }
  ];

  toggleContraste(): void {
    this.altoContraste = !this.altoContraste;
    console.log('Alto Contraste:', this.altoContraste);
  }

  toggleOscuro(): void {
    this.modoOscuro = !this.modoOscuro;
    console.log('Modo Oscuro:', this.modoOscuro);
  }

  toggleNotificaciones(): void {
    this.notificaciones = !this.notificaciones;
    console.log('Notificaciones:', this.notificaciones);
  }
}
