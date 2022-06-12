using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001277: Krend
/// </summary>
public class _11001277 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1208175407004832$
    // - Shush! You'll scare them off.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1208175407004835$
                // - Sorry, but now isn't a good time. As you can see, I'm busy.
                switch (selection) {
                    // $script:1208175407004836$
                    // - What are you up to?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1208175407004837$
                // - I'm collecting special materials. I'm a specialist in restoring old documents, antiques, and what have you. The secretions of the $npcNamePlural:21000074$ are important in my line of work. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
