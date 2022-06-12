using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000024: Lydia
/// </summary>
public class _11000024 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000133$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000136$
                // - Have you seen the Royal Road? Or rather, what's left of it? A huge earthquake tore right through it! Everyone who wants to get to $map:02000001$ is stuck here now.
                return 30;
            case (30, 1):
                // $script:0831180407000137$
                // - $map:02000001$ is so close, and yet so far. Those who came by ship to attend the court are beyond disappointed. That's why we've decided to open the mountain path. To those who are authorized to use it, of course.
                return -1;
            case (40, 0):
                // $script:1215093407009645$
                // - Hm? How may I help you?
                switch (selection) {
                    // $script:1215093407009646$
                    // - What can you tell me about trading airships?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1215093407009647$
                // - Oh! Well, there was some kind of new-old technological development that recently opened the skies to trade. Flying boats, what a concept!
                return 41;
            case (41, 1):
                // $script:1215093407009648$
                // - But, from what I've heard, only a fraction of the airships going out ever come back...
                switch (selection) {
                    // $script:1215093407009649$
                    // - What do you mean by that?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1215093407009650$
                // - The airships vanish into... well, thin air! Once they set off for the skies, they just don't come back.
                switch (selection) {
                    // $script:1215093407009651$
                    // - Does anyone know what happens to them?
                    case 0:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:1215093407009652$
                // - I haven't the faintest idea. Anyway, that's all I know.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
