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
