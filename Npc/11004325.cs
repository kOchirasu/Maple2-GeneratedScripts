using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004325: Blake
/// </summary>
public class _11004325 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1010140307011499$
    // - Breathtaking!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011500$
                // - Ahh... It's too beautiful.
                return 10;
            case (10, 1):
                // $script:1010140307011501$
                // - Can't you feel it? The stunning aurora in the sky... The alien wildlife... This place is filling me with creative energy!
                return 10;
            case (10, 2):
                // $script:1010140307011502$
                // - I feel it brewing inside. I'm ready to write a smash hit song!
                switch (selection) {
                    // $script:1010140307011503$
                    // - Since when do you write your own songs?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1010140307011504$
                // - Forget the $npcName:11004325[gender:0]$ you used to know. From this day on, I'm reborn as a guy who totally writes his own songs!
                return 20;
            case (20, 1):
                // $script:1010140307011505$
                // - You just wait. The new and improved $npcName:11004325[gender:0]$ is going to take the world by storm!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
