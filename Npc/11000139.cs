using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000139: Lailai
/// </summary>
public class _11000139 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407000565$
    // - Bah, what now?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000569$
                // - Hmph, this used to be a really nice place to live before that gigantic hotel dropped from the sky. It's been attracting all kinds of things and making our lives miserable.
                return -1;
            case (50, 0):
                // $script:0831180407000570$
                // - Well, I'm not fighting those monsters. It's not that they're too scary... I just don't want to be bothered.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
