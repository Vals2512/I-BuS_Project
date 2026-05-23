import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-gestionar-rutas',
  imports: [ReactiveFormsModule, RouterModule],
  templateUrl: './gestionar-rutas.html',
  styleUrl: './gestionar-rutas.scss',
})
export class GestionarRutas implements OnInit {
  rutaForm!: FormGroup;

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.rutaForm = this.fb.group({
      buscar: [''],
      idRuta: ['R - 10'],
      nombreRuta: ['Ruta Universitaria'],
      horario: ['05:00 - 22:00'],
      frecuencia: ['10 min'],
      empresa: ['Cootradelsol'],
      barrios: ['Centro, Laguito, UPTC, Terminal...'],
    });
  }

  onSubmit(): void {
    console.log('Ruta editada:', this.rutaForm.value);
  }

  onEliminar(): void {
    console.log('Eliminando ruta...');
  }
}
