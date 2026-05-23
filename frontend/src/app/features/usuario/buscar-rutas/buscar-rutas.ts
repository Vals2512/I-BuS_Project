import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-buscar-rutas',
  imports: [CommonModule, ReactiveFormsModule, RouterModule],
  templateUrl: './buscar-rutas.html',
  styleUrl: './buscar-rutas.scss',
})
export class BuscarRutas implements OnInit {
  buscarForm!: FormGroup;
  mostrarDetalleRuta = false;

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.buscarForm = this.fb.group({
      origen: ['Universidad Pedagógica ...'],
      destino: ['Calle 4 # 12 - 20'],
    });
  }

  buscarRuta(): void {
    // Simulamos que encuentra la ruta y despliega el panel
    this.mostrarDetalleRuta = true;
  }

  cerrarDetalle(): void {
    this.mostrarDetalleRuta = false;
  }
}
