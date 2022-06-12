using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000255: Rosetta
/// </summary>
public class _11000255 : NpcScript {
    protected override int First() {
        return 1;
    }

    // Select 0:
    // $script:0831180610000397$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // functionID=1 
                // $script:0831180610000400$
                // - $MyPCName$, how shall we style your hair today? Anything you like, just say the word.
                switch (selection) {
                    // $script:0831180610000401$
                    // - Anything? Really? Well, in that case...
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
