using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003157: Karen
/// </summary>
public class _11003157 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0306155707008050$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0306155707008053$
                // - You want to know the secret to a beautiful garden? Take care of your plants with love, and they'll repay you by growing.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
