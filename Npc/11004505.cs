using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004505: Mannstad Sentry
/// </summary>
public class _11004505 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012429$
    // - Identify yourself!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012430$
                // - Identify yourself!
                switch (selection) {
                    // $script:1228182607012431$
                    // - Whoa, there. I'm a friend!
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1228182607012432$
                // - Hey, you're that outlander. I read a report on you.
                return 11;
            case (11, 1):
                // $script:1228182607012433$
                // - Sorry if I seem on edge. Not all of the outlanders have been as... helpful as you.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
