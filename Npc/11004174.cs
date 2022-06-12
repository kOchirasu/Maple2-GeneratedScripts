using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004174: Blake
/// </summary>
public class _11004174 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010610$
    // - You don't have to look twice. I'm who you think I am.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010611$
                // - You're lucky to have run into me. I'm not sticking around, I've just popped in for a photo shoot. I can't really have a relaxing vacation with so many frenzied fans around.
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
