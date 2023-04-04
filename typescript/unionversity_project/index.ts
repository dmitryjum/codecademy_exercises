import courses from "./courses";
import studyGroups from "./studyGroups";

type Course = {
  id: number;
  studyGroupId: number;
  title: string;
  keywords: string[];
  eventType: string;
}

type StudyGroup = {
  id: number;
  courseId: number;
  title: string;
  keywords: string[];
  eventType: string;
}

type SearchEventsOptions = {
  query: string | number,
  eventType: string
}

function searchEvents(options: SearchEventsOptions) {
  let events: (Course | StudyGroup)[];
  events = options.eventType === 'courses' ? courses : studyGroups
  return events.filter((event: Course | StudyGroup) => {
    if (typeof(options.query) === 'number') {
      return event.id === options.query
    }

    if (typeof(options.query) === 'string') {
      return event.keywords.includes(options.query)
    }
  })
}

let enrolledEvents: (Course | StudyGroup)[] = [];

function enroll(...events: (Course | StudyGroup)[]) {
  events.forEach(e => enrolledEvents.push(e));
}

let searchResults = searchEvents({query: 'art', eventType: 'courses'});
enroll(searchResults[0], searchResults[1]);
console.log(enrolledEvents);