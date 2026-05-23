import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-gestionar-detalle-ruta',
  imports: [ReactiveFormsModule, RouterModule],
  templateUrl: './gestionar-detalle-ruta.html',
  styleUrl: './gestionar-detalle-ruta.scss',
})
export class GestionarDetalleRuta implements OnInit {
  detalleForm!: FormGroup;

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.detalleForm = this.fb.group({
      buscar: [''],
      idRuta: ['1', [Validators.required]],
      idTiempo: ['1', [Validators.required]],
      cantidadPasajeros: ['45', [Validators.required, Validators.min(0)]],
    });
  }

  onSubmit(): void {
    if (this.detalleForm.valid) {
      console.log('Detalle guardado:', this.detalleForm.value);
    }
  }

  onEliminar(): void {
    console.log('Eliminando detalle...');
  }
}
