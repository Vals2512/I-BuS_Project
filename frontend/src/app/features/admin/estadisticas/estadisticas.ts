import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-estadisticas',
  imports: [RouterModule],
  templateUrl: './estadisticas.html',
  styleUrl: './estadisticas.scss',
})
export class Estadisticas {
  totalRutas = 12;
  totalBarrios = 45;
  totalEmpresas = 4;
  usuariosActivos = 1240;
}
