using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000187: Maneh
/// </summary>
public class _11000187 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000818$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000820$
                // - I want nothing to do with the empress or her army. They were supposed to protect us! Instead everyone was frozen by ice elementals.
                return 20;
            case (20, 1):
                // $script:0831180407000821$
                // - My granddaughter was one of the victims. If... if the empire had just done something about the shadow gate the moment it opened, my son and his wife would still be here, safe and happy with me. 
                switch (selection) {
                    // $script:0831180407000822$
                    // - What's the story with the shadow gate?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180407000823$
                // - The Shadow Gate is the entrance to a world of demons who serve the darkness. The empire is trying to keep their evil contained.
                return 21;
            case (21, 1):
                // $script:0831180407000824$
                // - But I don't know... Closing the Shadow Gate at the cost of innocent lives... Is that really the right way to protect the world?
                return 21;
            case (21, 2):
                // $script:0831180407000825$
                // - My son and his wife could be still alive somewhere on the other side of the Shadow Gate. If it is closed, I'll never see them again.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Next,
            (21, 1) => NpcTalkButton.Next,
            (21, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
