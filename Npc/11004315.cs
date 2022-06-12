using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004315: Nairin
/// </summary>
public class _11004315 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0928133807011356$
    // - Would you like to take on a mission for Green Hoods?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0928133807011357$
                // - Our survey teams encountered some mechanical trees during their exploration of Kritias. Just hearing about it gives me the creeps. Who would build such a thing?
                return -1;
            case (20, 0):
                // $script:0116153807012735$
                // - Sorry, but I don't have any missions just yet.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
