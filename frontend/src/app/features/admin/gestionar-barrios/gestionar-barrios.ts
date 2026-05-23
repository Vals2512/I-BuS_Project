import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-gestionar-barrios',
  imports: [ReactiveFormsModule, RouterModule],
  templateUrl: './gestionar-barrios.html',
  styleUrl: './gestionar-barrios.scss',
})
export class GestionarBarrios implements OnInit {
  barrioForm!: FormGroup;
  rutasAsignadas = ['Ruta - 10', 'Ruta - 10', 'Ruta - 10'];

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.barrioForm = this.fb.group({
      buscar: [''],
      idBarrio: ['B - 24'],
      nombreBarrio: ['El Laguito'],
    });
  }

  onSubmit(): void {
    console.log('Barrio editado:', this.barrioForm.value);
  }

  onEliminar(): void {
    console.log('Eliminando barrio...');
  }

  quitarRuta(index: number): void {
    this.rutasAsignadas.splice(index, 1);
  }

  agregarRuta(): void {
    this.rutasAsignadas.push('Ruta - 10');
  }
}
