using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000071: Dixon
/// </summary>
public class _11000071 : NpcScript {
    protected override int First() {
        return 1;
    }

    // Select 0:
    // $script:0831180610000379$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // functionID=1 
                // $script:0831180610000383$
                // - Oooh, $MyPCName$, I'm so glad you found me. I can work miracles! Everyone says so. Now, what did you have in mind?
                switch (selection) {
                    // $script:0831180610000384$
                    // - Show me the possibilities.
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
