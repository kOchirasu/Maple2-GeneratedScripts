using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004374: Bobo
/// </summary>
public class _11004374 : NpcScript {
    internal _11004374(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011785$ 
                // - You want presents? Hee hee.
                return true;
            case 10:
                // $script:1109213607011786$ 
                // - You want presents? Hee hee.
                switch (selection) {
                    // $script:1120173007011859$
                    // - Never mind, I don't want it.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:1120173007011860$
                    // - I want it.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:1120173007011861$ 
                // - $npcName:11004349[gender:0]$ do better now. $npcName:11004349[gender:0]$ is sad.
                return true;
            case 12:
                // $script:1120173007011862$ 
                // - What want? $npcName:11004349[gender:0]$ do best!
                switch (selection) {
                    // $script:1120173007011863$
                    // - $npcName:11004349[gender:0]$'s big heart is enough.
                    case 0:
                        Id = 13;
                        return false;
                    // $script:1120173007011864$
                    // - How about a million mesos?
                    case 1:
                        Id = 14;
                        return false;
                }
                return true;
            case 13:
                // $script:1120173007011865$ 
                // - $MyPCName$... better than Santa! $npcName:11004349[gender:0]$ happy!
                return true;
            case 14:
                // $script:1120173007011866$ 
                // - Sorry... $npcName:11004349[gender:0]$ no money. Sniff... Sorry. Very sorry.
                switch (selection) {
                    // $script:1120173007011867$
                    // - $npcName:11004349[gender:0]$'s big heart is enough.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
