using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000033: Jorge
/// </summary>
public class _11000033 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0831180407000185$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000188$
                // - Ancient tomes containing stories of this world must be handled with care. They can teach us many important lessons.
                return -1;
            case (40, 0):
                // $script:0530154307008539$
                // - Are you lost? Why are you bothering me?
                switch (selection) {
                    // $script:0530154307008540$
                    // - Take me to $map:52000133$.
                    case 0:
                        return 41;
                    // $script:0530154307008541$
                    // - Just thought I'd pay you a social visit.
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // functionID=1 
                // $script:0530154307008542$
                // - $npcName:11000031[gender:0]$ says you're all right, so fine. Off you go.
                return -1;
            case (42, 0):
                // $script:0530154307008543$
                // - All right, then. I hope you're enjoying $map:02000023$.
                return -1;
            case (50, 0):
                // $script:0530154307008544$
                // - The ancient records of our history must be handled with care. They teach us many important lessons.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
