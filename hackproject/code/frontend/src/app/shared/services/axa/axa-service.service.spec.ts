import { TestBed } from '@angular/core/testing';

import { AxaServiceService } from './axa-service.service';

describe('AxaServiceService', () => {
  let service: AxaServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AxaServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
