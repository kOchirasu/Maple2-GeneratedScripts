using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001674: Bravos
/// </summary>
public class _11001674 : NpcScript {
    internal _11001674(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006397$ 
                // - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
                return true;
            case 30:
                // $script:0629000607006400$ 
                // - Do you have business with me? Hm?
                switch (selection) {
                    // $script:0629000607006401$
                    // - Tell me about yourself.
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0629000607006402$
                    // - What do you know about the $map:52000034$?
                    case 1:
                        Id = 70;
                        return false;
                    // $script:0706165507006631$
                    // - What happened to the vagrants Blackstar took hostage?
                    case 2:
                        Id = 80;
                        return false;
                    // $script:0712221207006725$
                    // - Tell me about $npcName:11001547[gender:0]$.
                    case 3:
                        Id = 90;
                        return false;
                }
                return true;
            case 40:
                // $script:0708181707006654$ 
                // - How about this. You know why they call me $npcName:11001674[gender:0]$?
                switch (selection) {
                    // $script:0708181707006655$
                    // - No clue.
                    case 0:
                        Id = 50;
                        return false;
                    // $script:0708181707006656$
                    // - Yes.
                    case 1:
                        Id = 60;
                        return false;
                }
                return true;
            case 50:
                // $script:0629000607006403$ 
                // - I'm so great I deserve a standing ovation! Haw! I can't believe you never heard of me. Well, remember me for next time.
                switch (selection) {
                    // $script:0708181707006657$
                    // - I heard your real name is Brav-gross.
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0629000607006404$ 
                // - Has somebody been tarnishing my good name? It's $npcName:11001682[gender:0]$, isn't it?
                // $script:0708181707006658$ 
                // - Ahem! I don't know where you heard that, but it's a dirty lie. $npcName:11001674[gender:0]$ is my name, and $npcName:11001674[gender:0]$ is who I am. Now get outta here, before you make me mad!
                switch (selection) {
                    // $script:0708225907006698$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 60:
                // $script:0629000607006405$ 
                // - You probably already heard this, but listen anyway. They call me Bravos 'cause I'm so great I deserve a standing ovation! Get it?
                switch (selection) {
                    // $script:0708181707006659$
                    // - I heard your real name is Brav-gross.
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:0629000607006406$ 
                // - Has somebody been tarnishing my good name? It's $npcName:11001682[gender:0]$, isn't it?
                // $script:0708181707006660$ 
                // - Ahem! I don't know where you heard that, but it's a dirty lie. $npcName:11001674[gender:0]$ is my name, and $npcName:11001674[gender:0]$ is who I am. Now get outta here, before you make me mad!
                switch (selection) {
                    // $script:0708225907006699$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 70:
                // $script:0706165507006632$ 
                // - I don't know, exactly. I heard we were gonna set up a base of operations in $map:02000001$, but there were problems with the construction. Eventually we gave up on the building, and... Well, take a look around you.
                switch (selection) {
                    // $script:0706165507006633$
                    // - Blackstar is moving in on $map:02000001$?
                    case 0:
                        Id = 71;
                        return false;
                }
                return true;
            case 71:
                // $script:0706165507006634$ 
                // - You really have no idea how big Blackstar is, do you? Every gangster in the underworld is connected to it one way or another. Gray Wolf or not, you can't take it on by yourself.
                switch (selection) {
                    // $script:0708181707006661$
                    // - How big is your organization, really?
                    case 0:
                        Id = 72;
                        return false;
                }
                return true;
            case 72:
                // $script:0708181707006662$ 
                // - Why do you care? That's none of your business. Now, I'd say that's enough stupid questions out of you.
                switch (selection) {
                    // $script:0708225907006700$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 80:
                // $script:0708181707006663$ 
                // - How should I know? It wasn't my operation. I don't even know where they are. I know you made some sorta deal with the boss, but let me give you some advice anyway: don't do anything stupid.
                // $script:0708181707006664$ 
                // - What I wanna know is why you're going along with whatever the boss says. A strong fighter like you could take Blackstar for $male:himself,female:herself$ if $male:he,female:she$ wanted. Maybe you just don't have the guts.
                switch (selection) {
                    // $script:0708181707006665$
                    // - I'm just afraid for their safety.
                    case 0:
                        Id = 81;
                        return false;
                }
                return true;
            case 81:
                // $script:0708181707006666$ 
                // - Yeah, sure you are. And that's the only reason you wanna know?
                switch (selection) {
                    // $script:0708181707006667$
                    // - I lost the match. I'm honor bound to work with him.
                    case 0:
                        Id = 82;
                        return false;
                }
                return true;
            case 82:
                // $script:0708181707006668$ 
                // - You're a bigger fool than $npcName:11001682[gender:0]$. Well, I guess I can't hold it against you if it means you're working <i>with</i> us instead of <i>against</i> us.
                switch (selection) {
                    // $script:0708225907006701$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 90:
                // $script:0712221207006726$ 
                // - You've come to the right man. What do you wanna know?
                switch (selection) {
                    // $script:0712221207006727$
                    // - Does $npcName:11001618[gender:0]$ get along with $npcName:11001547[gender:0]$?
                    case 0:
                        Id = 91;
                        return false;
                }
                return true;
            case 91:
                // $script:0712221207006728$ 
                // - Maybe you didn't know this, but $npcName:11001547[gender:0]$ is the boss's son. Heir to the kingdom, though you wouldn't know it to talk to him. All the officers sure seem to like him, though.
                switch (selection) {
                    // $script:0712221207006729$
                    // - And why is that?
                    case 0:
                        Id = 92;
                        return false;
                }
                return true;
            case 92:
                // $script:0712221207006730$ 
                // - You ever meet a boss's kid before? You know the type. Throws his daddy's weight around. Makes all the company goons do whatever he says. Well, $npcName:11001547[gender:0]$ ain't like that. He doesn't care about power or money. So why wouldn't they like him?
                switch (selection) {
                    // $script:0712221207006731$
                    // - And what does the rank-and-file think?
                    case 0:
                        Id = 93;
                        return false;
                }
                return true;
            case 93:
                // $script:0712221207006732$ 
                // - $npcName:11001547[gender:0]$ is our hero. His pop's the head honcho, but $npcName:11001547[gender:0]$ didn't ever get nothing that he didn't earn with his own two fists. A real man's man, you know?
                switch (selection) {
                    // $script:0712221207006733$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
