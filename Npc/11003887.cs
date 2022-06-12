using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003887: Ishura
/// </summary>
public class _11003887 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009927$
    // - Do you have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009928$
                // - Do you have something to say to me?
                return -1;
            case (30, 0):
                // $script:0515102507009929$
                // - Not bad.
                //   On behalf of Terrun Calibre, please accept my thanks.
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
