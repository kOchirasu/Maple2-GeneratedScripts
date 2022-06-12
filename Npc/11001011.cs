using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001011: Navue
/// </summary>
public class _11001011 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003450$
    // - Well, there goes the neighborhood.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003453$
                // - My realtor said that I'd only hear the sound of waves. I wouldn't have come here if I knew my neighbors would be so terrible.
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
