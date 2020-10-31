import re
import string
import sys
import colorama


DEBUG = True


class Error(Exception):
@@ -656,6 +660,9 @@ def _AppendRecord(self):
      cur_record[cur_record.index(None)] = ''

    self._result.append(cur_record)
    if DEBUG:
        print("{}{}: {}".format(colorama.Fore.BLUE, "RECORD > ", cur_record))
        print(colorama.Style.RESET_ALL)
    self._ClearRecord()

  def _Parse(self, template):
@@ -930,13 +937,19 @@ def _CheckLine(self, line):
      if matched:
        for value in matched.groupdict():
          self._AssignVar(matched, value)
          if DEBUG:
            print("{}{}: {}".format(colorama.Fore.GREEN, "Assign Var > ", value))
            print(colorama.Style.RESET_ALL)

        if self._Operations(rule, line):
          # Not a Continue so check for state transition.
          if rule.new_state:
            if rule.new_state not in ('End', 'EOF'):
              self._cur_state = self.states[rule.new_state]
            self._cur_state_name = rule.new_state
            if DEBUG:
              print("{}{}: {}".format(colorama.Fore.RED, "State Transition > ", rule.new_state))
              print(colorama.Style.RESET_ALL)
          break

  def _CheckRule(self, rule, line):

