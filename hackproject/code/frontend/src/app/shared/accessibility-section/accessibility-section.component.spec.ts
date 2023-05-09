import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AccessibilitySectionComponent } from './accessibility-section.component';

describe('AccessibilitySectionComponent', () => {
  let component: AccessibilitySectionComponent;
  let fixture: ComponentFixture<AccessibilitySectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AccessibilitySectionComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AccessibilitySectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
