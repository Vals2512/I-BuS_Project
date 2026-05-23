import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-panel-ajustes',
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './panel-ajustes.html',
  styleUrl: './panel-ajustes.scss',
})
export class PanelAjustes {
  altoContraste = true;
  modoOscuro = true;
  notificaciones = true;
  tamanoTexto = 50;

  toggleContraste(): void {
    this.altoContraste = !this.altoContraste;
  }

  toggleOscuro(): void {
    this.modoOscuro = !this.modoOscuro;
  }

  toggleNotificaciones(): void {
    this.notificaciones = !this.notificaciones;
  }
}
