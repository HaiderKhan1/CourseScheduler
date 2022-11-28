import Scheduler from '../Scheduler';
import { shallow } from 'enzyme';
import ChakraSelect from 'chakra-react-select';
import FullCalendar from '@fullcalendar/react';
import { screen } from '@testing-library/dom';

describe('Scheduler', () => {
  it('renders the scheduler component without crashing', () => {
    shallow(<Scheduler />);
  });

  // Ensure calendar is there on render
  it('contains a fullcalendar on render', () => {
    const wrapper = shallow(<Scheduler />);
    const calendar = wrapper.find(FullCalendar);
    expect(calendar.length).toEqual(1);
  });

  // Ensure dropdown is there on render
  it('contains a dropdown for selecting semester', () => {
    const wrapper = shallow(<Scheduler />);
    expect(wrapper.find('#semesterSelect').length).toEqual(1);
  });
});
