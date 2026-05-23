import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PanelAjustes } from './panel-ajustes';

describe('PanelAjustes', () => {
  let component: PanelAjustes;
  let fixture: ComponentFixture<PanelAjustes>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PanelAjustes],
    }).compileComponents();

    fixture = TestBed.createComponent(PanelAjustes);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
