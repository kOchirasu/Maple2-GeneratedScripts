using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004374: Bobo
/// </summary>
public class _11004374 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011785$
    // - You want presents? Hee hee.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011786$
                // - You want presents? Hee hee.
                switch (selection) {
                    // $script:1120173007011859$
                    // - Never mind, I don't want it.
                    case 0:
                        return 11;
                    // $script:1120173007011860$
                    // - I want it.
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:1120173007011861$
                // - $npcName:11004349[gender:0]$ do better now. $npcName:11004349[gender:0]$ is sad.
                return -1;
            case (12, 0):
                // $script:1120173007011862$
                // - What want? $npcName:11004349[gender:0]$ do best!
                switch (selection) {
                    // $script:1120173007011863$
                    // - $npcName:11004349[gender:0]$'s big heart is enough.
                    case 0:
                        return 13;
                    // $script:1120173007011864$
                    // - How about a million mesos?
                    case 1:
                        return 14;
                }
                return -1;
            case (13, 0):
                // $script:1120173007011865$
                // - $MyPCName$... better than Santa! $npcName:11004349[gender:0]$ happy!
                return -1;
            case (14, 0):
                // $script:1120173007011866$
                // - Sorry... $npcName:11004349[gender:0]$ no money. Sniff... Sorry. Very sorry.
                switch (selection) {
                    // $script:1120173007011867$
                    // - $npcName:11004349[gender:0]$'s big heart is enough.
                    case 0:
                        return 13;
                }
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            (14, 0) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
