using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000374: Tann
/// </summary>
public class _11000374 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;60
    }

    // Select 0:
    // $script:0831180407001534$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001537$
                // - What?
                switch (selection) {
                    // $script:0831180407001538$
                    // - So uh... are you a dude or a lady?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407001539$
                // - Think what you like!
                return -1;
            case (60, 0):
                // $script:0831180407001540$
                // - There are treasure chests hidden all over the world. How did they get there? Who knows and who cares! Just remember the golden rule: finders keepers!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
