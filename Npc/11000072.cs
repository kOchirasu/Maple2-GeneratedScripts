using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000072: Zenko
/// </summary>
public class _11000072 : NpcScript {
    protected override int First() {
        return 1;
    }

    // Select 0:
    // $script:0831180610000385$
    // - How can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // functionID=1 
                // $script:0831180610000389$
                // - Welcome, $MyPCName$. Thinking about spicing up your look? I can give you any skin tone you like. Care to take a peek?
                switch (selection) {
                    // $script:0831180610000390$
                    // - Yeah, let's do it!
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
