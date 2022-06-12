using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003885: Eupheria
/// </summary>
public class _11003885 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009921$
    // - Our investigation continues.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009922$
                // - Our investigation continues.
                return -1;
            case (30, 0):
                // $script:0515102507009923$
                // - Thank you. I think I've started to unravel the truth.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
