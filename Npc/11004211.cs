using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004211: Pupu
/// </summary>
public class _11004211 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806052107010676$
    // - Yaaawn...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806052107010677$
                // - ♬I wanna be where the mushfolk are. I wanna see—wanna see 'em mushin'.
                //   Bouncin' around on those stalks!♬
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
