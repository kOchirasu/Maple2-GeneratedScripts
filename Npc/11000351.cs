using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000351: Mirror
/// </summary>
public class _11000351 : NpcScript {
    protected override int First() {
        return 0;
    }

    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (0, 0):
                // functionID=1 
                // $script:0831180610000437$
                // - Just look at that gorgeous reflection! Can you believe that's you?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (0, 0) => NpcTalkButton.SelectableBeauty,
            _ => NpcTalkButton.None,
        };
    }
}
