using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004209: Humhum
/// </summary>
public class _11004209 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806045807010664$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806045807010665$
                // - Hmm? Is that really the $npc:11004213[gender:0]$, you ask? Yep! Except this one is bigger. Otherwise, they're identical in every way! The real $npc:11004213[gender:0]$ is full of hot air, too, heh heh heh!
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
