using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003081: Seaside Cabin
/// </summary>
public class _11003081 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0113143107007762$
    // - <font color="#909090">(You see a wooden cabin weathered by wind and sea.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0113143107007763$
                // - <font color="#909090">(Is someone inside this cabin? You can hear voices.)</font>
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
