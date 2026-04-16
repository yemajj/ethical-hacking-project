// progress.js — localStorage helpers for lesson completion and notes

const PROGRESS_KEY = 'cyberEduProgress';

function getProgress() {
  return JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{}');
}

function isComplete(lessonId) {
  return getProgress()[lessonId] === true;
}

function markComplete(lessonId) {
  const p = getProgress();
  p[lessonId] = true;
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(p));
}

function unmarkComplete(lessonId) {
  const p = getProgress();
  delete p[lessonId];
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(p));
}

function saveNote(lessonId, text) {
  localStorage.setItem('note_' + lessonId, text);
}

function loadNote(lessonId) {
  return localStorage.getItem('note_' + lessonId) || '';
}
