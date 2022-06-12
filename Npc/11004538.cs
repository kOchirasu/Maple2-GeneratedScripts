using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004538: Barricade Defender
/// </summary>
public class _11004538 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0104170807012616$
    // - Zzz zzz...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0104170807012617$
                // - Zzz zzz...
                return 10;
            case (10, 1):
                // $script:0104170807012618$
                // - Wha? Huh? I'm defendin'... I'm defendin' the base!
                return 10;
            case (10, 2):
                // $script:0104170807012619$
                // - Here I figured I'd spend my last years of my service in the capital, then retire and spend the rest of my days on a little farm out by Evansville. But nooo, they had to ship me out to this light-forsaken place... 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
