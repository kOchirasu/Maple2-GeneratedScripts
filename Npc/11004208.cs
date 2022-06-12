using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004208: Tumtum
/// </summary>
public class _11004208 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806045807010658$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806045807010659$
                // - The mush before you is merely a facsimile of his mushyness. The real $npc:11004213[gender:1]$ is actually luxuriating inside the castle.
                switch (selection) {
                    // $script:0806045807010660$
                    // - A facsimile?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0806045807010661$
                // - Fake. A fraud. A phony. See the way he bounces around? It's really just an inflatable balloon rigged up to make noises.
                switch (selection) {
                    // $script:0806045807010662$
                    // - That's a pretty lifelike balloon.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0806045807010663$
                // - I know, right? You can touch him, if you want. Just don't pop him. These things are expensive.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
