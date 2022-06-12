using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003824: Strange Claw Marks
/// </summary>
public class _11003824 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0116111107009757$
    // - <font color="#909090">(There's an odd grouping of large claw marks here.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0116111107009758$
                // - <font color="#909090">(There's an odd grouping of large claw marks here.)</font>
                return 10;
            case (10, 1):
                // $script:0116111107009759$
                // - <font color="#909090">(This must have been left by a $npcName:11003781[gender:0]$.)</font>
                switch (selection) {
                    // $script:0116111107009760$
                    // - (Take a picture.)
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0116111107009761$
                // - <font color="#909090">(This might be a clue. You take a picture of the markings to show them to $npcName:11003536[gender:0]$.)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
