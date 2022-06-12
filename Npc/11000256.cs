using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000256: Ren
/// </summary>
public class _11000256 : NpcScript {
    protected override int First() {
        return 1;
    }

    // Select 0:
    // $script:0831180610000402$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // functionID=1 
                // $script:0831180610000406$
                // - Nothing expresses the inner YOU like carefully-selected cosmetics. How'd you like to experiment with a new look?
                switch (selection) {
                    // $script:0831180610000407$
                    // - Yep, time to accessorize!
                    case 0:
                        return 0;
                }
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (1, 0) => NpcTalkButton.SelectableBeauty,
            _ => NpcTalkButton.None,
        };
    }
}
