import { DOCUMENT } from '@angular/common';
import { Inject, Injectable } from '@angular/core';
import { THEMES } from './theme';

@Injectable({
  providedIn: 'root',
})
export class ThemeServiceService {
  constructor(@Inject(DOCUMENT) private document: Document) {}

  setTheme(name = 'Default') {
    const theme:any = THEMES[name];
    Object.keys(theme).forEach((key) => {
      this.document.documentElement.style.setProperty(`--${key}`, theme[key]);
    });
  }

  changeThemeToDark(name:any){
    console.log(name)
    const theme:any = THEMES[name];
    Object.keys(theme).forEach((key) => {
      this.document.documentElement.style.setProperty(`--${key}`, theme[key]);
    });
  }

}
