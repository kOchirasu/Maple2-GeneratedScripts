using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001376: Pallard
/// </summary>
public class _11001376 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217144507005361$
    // - You called?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217144507005364$
                // - Mwahaha! This scene is... perfect! The height of drama, eclipsing any movie or show I've ever seen! And <i>I'm</i> the guy who gets to film it. This is probably going to be the greatest film of my entire career!
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
