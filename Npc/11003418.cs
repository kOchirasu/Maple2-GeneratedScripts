using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003418: Screaming Fist
/// </summary>
public class _11003418 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008623$
    // - 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008624$
                // - 
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
