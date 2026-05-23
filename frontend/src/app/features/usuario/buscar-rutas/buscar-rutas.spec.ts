import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BuscarRutas } from './buscar-rutas';

describe('BuscarRutas', () => {
  let component: BuscarRutas;
  let fixture: ComponentFixture<BuscarRutas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BuscarRutas],
    }).compileComponents();

    fixture = TestBed.createComponent(BuscarRutas);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
